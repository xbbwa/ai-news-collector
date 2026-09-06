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
         ── reddit（公开 Atom 订阅源 /r/<sub>/<listing>/.rss，无需账号；进程内串行、间隔 61s 以避开匿名限流）
         ── huggingface（Hub 公开 API，按组织监控模型发布；国内大模型厂商唯一可机读的一手渠道）
        │
pipeline ── 关键词/时效过滤 → URL 归一化 + sha256 去重 → 入库 → 并发抓正文（trafilatura，favor_recall 尽量保留原文）
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
python -m collector once -s openai-news -s qbitai       # 只拉指定信源
python -m collector run              # 常驻调度
python -m collector api              # 启动 API，默认 :8000
python -m collector export --since-id 0 --out items.jsonl
python -m collector retry-extract    # 重试正文抽取失败的条目

python scripts/check_sources.py      # 信源体检：每个源实抓一次（不写库），报告条目数/过滤后保留数/最新时间/错误
python scripts/stats.py              # 各源入库数 / 抽取成功率 / 错误汇总
python scripts/probe.py <url> --feed # 排查某个 feed：状态码、内容预览、条目数
```

feed 会悄悄失效（本次审计就发现 3 个坏路由），建议每月跑一次 `check_sources.py`。

## 部署到 Ubuntu 服务器（Docker）

```bash
git clone https://github.com/xbbwa/ai-news-collector.git ~/ai-news-collector && cd ~/ai-news-collector
cp .env.example .env
# 编辑 .env：PROXY_URL 填服务器上可用的代理（如 http://host.docker.internal:7890）；没有代理就留空
docker compose up -d --build
docker compose logs -f collector
curl localhost:8000/health
docker compose exec api python scripts/check_sources.py    # 在容器里体检所有源（含 RSSHub 路由）
```

更新：`git pull && docker compose up -d --build`。数据库在 `./data/collector.db`（SQLite + WAL），**必须放本地磁盘，不能放 NFS**。

国内服务器的三个坑（prod-ubuntu 上实际踩过）：

- `git clone` GitHub 会卡死（网页能开、git 协议不通）。从本机推：`git archive --format=tar <commit> | ssh yino@192.168.110.111 "mkdir -p ~/ai-news-collector && tar -x -C ~/ai-news-collector"`，再把 commit 写进 `DEPLOYED_COMMIT`。
- Docker Hub 不通、镜像源列表里有死站时，`compose up` 会卡在拉镜像上毫无输出。先手动指定可用镜像源拉好再起：`docker pull docker.1panel.live/diygod/rsshub:latest && docker tag docker.1panel.live/diygod/rsshub:latest diygod/rsshub:latest`。
- pypi.org 一个请求 7 秒。`.env` 里设 `PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/` 再 build。

Compose 里包含四个服务：

| 服务 | 作用 |
| --- | --- |
| `collector` | 常驻调度采集 |
| `api` | HTTP API，端口 8000 |
| `rsshub` | 自建 RSSHub，把没有 RSS 的站点（Anthropic、DeepSeek、36氪、虎嗅、智源社区、HF Daily Papers）转成 RSS，端口 1200 |
| `redis` | RSSHub 缓存 |

### 给 OpenClaw 的每日 Markdown（prod-ubuntu 上的接法）

服务器上原来是 cron 每天 07:01 跑 `~/scripts/daily_ai_news.py`，把 4 个 RSS 各 5 条写成
`/mnt/data/openclaw-kb/openclawdata/daily-ai-news-summary.md`，OpenClaw 读这个文件做中文推送。
现在由 `scripts/daily_digest.py` 生成同一个文件：只依赖标准库，通过 API 取最近 24 小时的条目，按
Tier / 信源分组，每源最多 8 条，摘要截 400 字（原文节选，不翻译不清洗），文件头尾保留给 OpenClaw 的提示。

```bash
# crontab -e（yino），替换原来的 daily_ai_news.py 那一行
01 7 * * * /usr/bin/python3 /home/yino/ai-news-collector/scripts/daily_digest.py --out /mnt/data/openclaw-kb/openclawdata/daily-ai-news-summary.md >> /home/yino/ai-news-collector/data/digest.log 2>&1
```

条目太多影响推送质量时调 `--max-per-source` / `--hours`；下游要完整原文走 `GET /items?fetched_after=...`。

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
| `summary` | RSS 摘要（纯文本）；Reddit 自发帖正文；HF 模型的 pipeline/库/标签 |
| `content` | trafilatura 抽取的正文纯文本（favor_recall，宁多勿少，清洗交给下游） |
| `top_image` | 正文首图 URL（给后续视频配图用） |
| `published_at` / `fetched_at` | UTC ISO 时间 |
| `extract_status` | `ok` / `failed` / `pending` / `skipped` |
| `raw` | 来源特有字段，原样保留：RSS 原始 HTML 摘要 `summary_html` 和原始时间字符串 `published_raw`、tags；HN 分数/评论数；Reddit permalink/子版块/是否自发帖/缩略图；HF 模型的 likes/downloads/tags/创建与修改时间 |

## 信源说明

见 `config/sources.yaml`，72 个启用信源，按三层组织：

- **Tier 1 一手（国外）**：OpenAI、Anthropic（News/Engineering，RSSHub）、DeepMind、Google AI / Google Research / Google Cloud AI、Meta Engineering + Meta 新闻室、Hugging Face 博客、Microsoft Research、NVIDIA 博客 + 技术博客、AWS ML、Amazon Science、Apple ML Research、Mistral、GitHub 博客（Copilot）、Databricks、EleutherAI、arXiv（cs.AI/CL/LG/CV）、HF Daily Papers（RSSHub）、HF 模型发布（26 个国外机构：openai、meta-llama、google、microsoft、nvidia、mistralai、CohereLabs、allenai、stabilityai、black-forest-labs、apple、xai-org 等）
- **Tier 1 一手（国内）**：DeepSeek 官方新闻（RSSHub）、HF 模型发布（22 个国内机构：deepseek-ai、Qwen、Wan-AI、zai-org 智谱、moonshotai、MiniMaxAI、stepfun-ai、baichuan-inc、openbmb、internlm、OpenGVLab、tencent、ByteDance-Seed、baidu、XiaomiMiMo、inclusionAI 蚂蚁、Skywork、meituan-longcat、Kwai-Kolors、BAAI 等）。国内厂商没有一家提供 RSS，官网公告基本只发微信，HF 上的权重发布往往比新闻稿还早几小时，是目前唯一可机读的一手信号
- **Tier 2 媒体（国外）**：TechCrunch、The Verge、VentureBeat、MIT TR（AI 专栏）、Ars Technica、WIRED、The Guardian AI、IEEE Spectrum AI、The Decoder、MarkTechPost、Axios、CNBC、Bloomberg / NYT / FT（付费墙，只留标题摘要）、Nature ML；通讯：Import AI、SemiAnalysis、Latent Space、Interconnects、One Useful Thing、Ahead of AI、Simon Willison
- **Tier 2 媒体（国内）**：量子位、智东西、InfoQ、36氪快讯 + AI 频道（RSSHub）、虎嗅（RSSHub）、钛媒体、爱范儿、极客公园、IT之家、少数派、雷峰网、开源中国
- **Tier 3 社交/聚合**：Hacker News（22 个查询词）、Reddit 7 个板块合并（MachineLearning、LocalLLaMA、artificial、singularity、OpenAI、ClaudeAI、StableDiffusion；new + hot 两路）、GitHub Trending（公共 feed，无需 token）、Product Hunt AI、智源社区（RSSHub）

`proxy: true` 的源在国内服务器上走 `PROXY_URL`；`${RSSHUB_URL}` 的源必须保持 `proxy: false`（RSSHub 容器自己走 `PROXY_URI`，采集器到 RSSHub 是内网请求）。抓正文时先直连，遇到 403/503 换 Chrome 指纹重试，再失败切代理。

关键词过滤只用于泛科技源。英文关键词按整词匹配（`AI` 能命中 `AI芯片`、`AI-powered`、`AIGC`，不会命中 `said`、`Airbnb`、`aims`），中文关键词按子串匹配；`芯片`/`算力` 是刻意放宽的，会带进少量消费电子/半导体新闻，交给下游清洗。

实测（2026-09-06，`scripts/check_sources.py`）：本机直连 61 个源全部正常；HF 模型源一轮返回国内 429 / 国外 487 个模型，7 天内新增或更新的分别 41 / 72 个。prod-ubuntu（无代理）上 73 个启用源中 55 个正常，失败的全部是被墙站点：Hugging Face 三个源、Reddit 两个、Google Research / Cloud、Mistral、Import AI（substack.com 主域被墙，自定义域名的 Substack 都能通）、NYT、FT、Bloomberg、Guardian、Axios。**配上 `PROXY_URL` 这 13 个源就能恢复**，其中 HF 模型发布是国内厂商唯一的一手渠道，值得配。

整个项目**不需要任何账号或凭据**：所有信源都走公开接口，HTTP API 也不做鉴权。

### 已知限制

- **Reddit**：OAuth API 和 `.json` 接口都已要求登录，改用公开的 Atom 订阅源。Reddit 对匿名客户端限流为每 IP 每分钟 1 次请求，抓取器会在进程内把所有 Reddit 源串行并间隔 61s；因此用多板块合并（`a+b+c`）一次请求覆盖 7 个板块，`raw.subreddit` 仍记录每条帖子自己的板块。订阅源里没有分数和评论数。Chrome 指纹客户端反而会被 reddit.com 判为可疑返回 403，所以 Reddit 只用普通 httpx 客户端。
- **arXiv**：每日批次约 00:00 UTC（北京时间 8:00）发布，周日到周四；周五、周六 feed 为空，`check_sources.py` 里显示 0 条是正常的。
- **InfoQ 中文**：feed 把北京时间标成 GMT，配置里用 `time_offset_hours: -8` 修正；`raw.published_raw` 保留原始字符串。
- **HF 模型源**：按 `lastModified` 排序、`published_at` 也取修改时间，因为模型仓库通常先私有创建、发布时才公开并提交最后一次修改；老模型改一次 README 也会出现，靠 URL 去重只入库一次。google / microsoft / nvidia / facebook 会带进大量微调和研究产物，属预期噪音。
- **OpenAI 正文**：openai.com 在 Cloudflare 后面，普通请求 403；已内置 curl_cffi 指纹回退，实测可过。如果将来失效，需要上 Playwright。
- **付费墙**：Bloomberg、NYT、FT、Nature 只存标题和摘要（`fetch_fulltext: false`）。

### 没接入的

- **机器之心**：官网 RSS 已死，站点是纯前端应用无公开接口，RSSHub 也没有路由。配置里保留但 `enabled: false`；其报道通常一小时内被量子位、36氪、IT之家等转载。
- **晚点 LatePost**：站点的 Let's Encrypt 证书缺中间证书，RSSHub（Node）无法验证 TLS；`enabled: false`，等站点修好再开。
- **Anthropic Research**：RSSHub 路由当前返回空（页面改版）；News 和 Engineering 正常。`enabled: false`。
- **GitHub Trending**：RSSHub 路由强制要求 `GITHUB_ACCESS_TOKEN`，改用 mshibanami/GitHubTrendingRSS 的公共 feed。
- **微信公众号**（新智元、硅星人、甲子光年等）：所有桥接方案（WeWe RSS 等）都需要登录微信账号，不接入。
- **X/Twitter**：所有可用路线（RSSHub、Nitter）现在都需要登录账号，不接入。
- **Meta AI 博客 / Microsoft AI 博客 / xAI**：分别是 400、403、无 feed；Meta 靠 Engineering 博客 + 新闻室覆盖，Microsoft 靠 Research 博客，xAI 靠 HF `xai-org` 和媒体。
- 本次审计确认已失效、未加入的 feed：36kr.com/feed、jiqizhixin.com/rss、pingwest、latepost 官网、Stability AI、Cohere、Synced、WSJ Tech、ZDNet AI、Qwen 博客（github.io，一年未更新）。

## 加信源

在 `sources.yaml` 追加一条即可，无需改代码。通用站点用 `keywords` 过滤只留 AI 相关；已经是 AI 垂直源的不要加 `keywords`，避免漏掉。新增 HF 机构只需在 `hf-models-*` 的 `authors` 列表里加一行组织名（`huggingface.co/<org>` 的路径部分）。加完跑一次 `python scripts/check_sources.py <id>` 确认能抓到。
