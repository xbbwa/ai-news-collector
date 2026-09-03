# AI News Collector

AI 方向（国内外）新闻**采集层**：从 RSS / 官方 API 拉取原文，去重，抽取正文，存库，通过 HTTP API 增量输出给下游处理系统。

本项目**只做采集**，不做翻译、聚类、摘要、LLM 处理。输出是原文 + 元数据。

## 架构

```
config/sources.yaml  ── 信源清单（分层、轮询间隔、是否走代理、关键词过滤）
        │
scheduler ── 每个信源一个独立协程，按各自间隔轮询，失败指数退避
        │
fetchers ── rss（ETag / If-Modified-Since 条件请求）
         ── hackernews（Algolia 搜索 API）
         ── reddit（官方 OAuth API，需要 REDDIT_CLIENT_ID/SECRET）
        │
pipeline ── 关键词/时效过滤 → URL 归一化 + sha256 去重 → 入库 → 并发抓正文（trafilatura）
         ── 正文下载遇到 403/503（Cloudflare）自动切换 Chrome 指纹客户端（curl_cffi），再失败切代理
        │
SQLite / PostgreSQL  ── items 表，自增 id 即消费游标
        │
api ── GET /items?since_id=N  供下游增量拉取
```

## 快速开始（本机）

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env               # 按需修改 PROXY_URL / RSSHUB_URL

python -m collector sources          # 查看信源清单
python -m collector once             # 所有信源各拉一次
python -m collector once -s openai-news -s jiqizhixin   # 只拉指定信源
python -m collector run              # 常驻调度
python -m collector api              # 启动 API，默认 :8000
python -m collector export --since-id 0 --out items.jsonl
python -m collector retry-extract    # 重试正文抽取失败的条目

python scripts/stats.py              # 各源入库数 / 抽取成功率 / 错误汇总
python scripts/probe.py <url> --feed # 排查某个 feed：状态码、内容预览、条目数
```

## 部署到 Ubuntu 服务器（Docker）

```bash
cp .env.example .env
# 编辑 .env：PROXY_URL 填服务器上可用的代理（如 http://host.docker.internal:7890）
docker compose up -d --build
docker compose logs -f collector
curl localhost:8000/health
```

Compose 里包含四个服务：

| 服务 | 作用 |
| --- | --- |
| `collector` | 常驻调度采集 |
| `api` | HTTP API，端口 8000 |
| `rsshub` | 自建 RSSHub，把没有 RSS 的国内站点（36氪、极客公园、GitHub Trending、X 等）转成 RSS，端口 1200 |
| `redis` | RSSHub 缓存 |

## 下游对接

下游系统按游标增量拉取，`id` 单调递增，记住上次的 `next_since_id` 即可：

```
GET /items?since_id=0&limit=500
GET /items?since_id=0&tier=1                 # 只要一手来源
GET /items?since_id=0&extract_status=ok      # 只要正文抽取成功的
GET /items?since_id=0&include_content=false  # 不带正文，只要元数据
GET /items/{id}
GET /sources                                 # 各信源健康状态
GET /health
```

每条 item 字段：

| 字段 | 说明 |
| --- | --- |
| `id` | 自增游标 |
| `source_id` / `source_tier` | 来源及其层级（1 一手 / 2 媒体 / 3 社交） |
| `url` | 原文链接（已用于去重，去掉 utm 等追踪参数后做 sha256） |
| `title` / `author` / `lang` | 元数据 |
| `summary` | RSS 摘要（纯文本） |
| `content` | trafilatura 抽取的正文纯文本 |
| `top_image` | 正文首图 URL（给后续视频配图用） |
| `published_at` / `fetched_at` | UTC ISO 时间 |
| `extract_status` | `ok` / `failed` / `pending` / `skipped` |
| `raw` | 来源特有字段：HN 分数、Reddit 评论数、RSS 原始 HTML 摘要、tags 等 |

## 信源说明

见 `config/sources.yaml`，已按三层组织：

- **Tier 1 一手**：OpenAI、DeepMind、Google AI、Meta Engineering、Hugging Face、Microsoft Research、NVIDIA、AWS ML、Mistral、arXiv（cs.AI/CL/LG/CV）
- **Tier 2 媒体**：TechCrunch、The Verge、VentureBeat、MIT TR、Ars Technica、WIRED、The Decoder、Import AI、Bloomberg；国内：机器之心（RSSHub）、量子位、InfoQ、36氪（RSSHub）、虎嗅（RSSHub）、爱范儿、极客公园（RSSHub）、少数派、雷峰网
- **Tier 3 社交/聚合**：Hacker News（按关键词）、r/MachineLearning、r/LocalLLaMA、r/artificial、GitHub Trending（RSSHub）

`proxy: true` 的源在国内服务器上走 `PROXY_URL`。抓正文时先直连，遇到 403/503 换 Chrome 指纹重试，再失败切代理。

实测（2026-09-03，本机直连）：38 个源里除 RSSHub 路由（本机未起容器）和 Reddit（未配凭据）外全部正常，一轮 1184 条；直连媒体源正文抽取成功率 100%，Hacker News 外链约 90%（失败的是付费墙和 PDF）。

### 需要额外配置的

- **Reddit**：现在不登录直接 403。去 https://www.reddit.com/prefs/apps 建一个免费的 "script" 类型 app，把 id/secret 填进 `.env` 的 `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET`。
- **OpenAI 正文**：openai.com 在 Cloudflare 后面，普通请求 403；已内置 curl_cffi 指纹回退，实测可过。如果将来失效，需要上 Playwright。

### 还没接入、需要额外部署的

- **微信公众号**（新智元、硅星人、智东西等）：推荐在服务器上自建 [WeWe RSS](https://github.com/cooderl/wewe-rss)，然后把生成的 feed 加进 `sources.yaml`。
- **X/Twitter**：RSSHub 需要配置账号 cookie（compose 里有注释），配好后启用 `${RSSHUB_URL}/twitter/user/<name>` 路由。
- **Anthropic 官网**：没有 RSS，目前靠 Tier 2/3 覆盖（一般几分钟内就有转载）。

## 加信源

在 `sources.yaml` 追加一条即可，无需改代码。通用站点用 `keywords` 过滤只留 AI 相关；已经是 AI 垂直源的不要加 `keywords`，避免漏掉。
