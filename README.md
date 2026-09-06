# AI News Collector

AI 方向（国内外）新闻**采集层**：从 RSS / 官方 API 拉取原文，去重，抽取正文，按天归档成 JSONL 提交到 GitHub，下游从 GitHub 取。

本项目**只做采集**，不做翻译、聚类、摘要、LLM 处理。输出是原文 + 元数据。不需要任何账号、凭据或代理。

## 运行方式：两边抓、GitHub 合并，全文进私有归档仓、摘要发公开 `data` 分支

每个信源在 `sources.yaml` 里标了 `runner`：国外源和所有 RSSHub 路由走 GitHub Actions（美国 runner，HF / Reddit / Google 直连），
直连的国内媒体和对数据中心 IP 设防的站点（VentureBeat 限流、MarkTechPost 返回反爬页）走国内服务器（`runner: server`，
快、不会被海外 IP 拒绝）。两边各写各的文件，Actions 生成摘要时合并。

本仓库是**公开**的（Actions 分钟数不限），但采集到的是第三方文章**全文**，不能公开再分发，所以全文只进私有仓库
[xbbwa/ai-news-archive](https://github.com/xbbwa/ai-news-archive)，公开分支上只有标题 + 短摘要 + 链接的摘要文件；
两边工作库（SQLite）存在 `state` Release 里，用 `STATE_KEY` 加密后才上传。

```
GitHub Actions（每小时 :30，.github/workflows/collect.yml）          国内服务器（systemd 用户服务常驻）
   │ 1. 从 state Release 取回加密的 SQLite 工作库 + 游标，解密            │ python -m collector run（COLLECTOR_RUNNER=server，12 个源）
   │ 2. collector once（runner=github，63 源；RSSHub 作 service 容器）      │ cron :15  scripts/server_publish.sh
   │ 3. export_daily.py → 私有归档仓 items/YYYY-MM-DD.jsonl（deploy key）  │   export_daily.py → ~/ai-news-archive/items/YYYY-MM-DD.cn.jsonl
   │    daily_digest.py / curate_digest.py（合并 *.cn.jsonl，按 URL 去重） │   git push → 私有归档仓（SSH 走 443 端口 + deploy key）
   │    → 公开 data 分支 digest/latest.md、curated.md、curated.json        │
   │ 4. 库加密后 + 游标传回 state Release                                  │
   ▼                                                                    ▼
xbbwa/ai-news-archive（私有）── items/YYYY-MM-DD.jsonl（GitHub 侧） + items/YYYY-MM-DD.cn.jsonl（服务器侧），含正文
xbbwa/ai-news-collector data 分支（公开）── digest/latest.md、curated.md、curated.json、pushed-history.jsonl
   │
   ▼  纯 HTTPS 下载（raw.githubusercontent.com）
国内服务器 ── cron 07:01：scripts/sync_digest.sh 把摘要放到 OpenClaw 读的位置，并回传 pushed-history.jsonl
```

两侧文件名不同所以永不冲突；推送前都会 `git pull --rebase`。两侧各自去重，同一篇文章被两边不同信源抓到时归档里会各有一条
（摘要里按 URL 去重）。`id` 是各自数据库的自增号，跨文件不唯一，下游按 `fetched_at` 或文件内顺序取增量。

消费数据：

```
公开（匿名可下）：
https://raw.githubusercontent.com/xbbwa/ai-news-collector/data/digest/latest.md
https://raw.githubusercontent.com/xbbwa/ai-news-collector/data/digest/curated.md
备用：https://api.github.com/repos/xbbwa/ai-news-collector/contents/digest/latest.md?ref=data  （Accept: application/vnd.github.raw）

全文（私有仓，需要有该仓库读权限的 PAT 或 deploy key）：
https://raw.githubusercontent.com/xbbwa/ai-news-archive/main/items/2026-09-06.jsonl   -H "Authorization: Bearer $TOKEN"
```

手动触发一次：`gh workflow run collect`；看运行：`gh run list --workflow collect`。仓库公开，Actions 分钟数不限；
定时任务实际触发会比 cron 晚 5–15 分钟，`30 * * * *` 的 22:30 UTC 那一轮正好落在 07:01 北京时间的拉取之前。

工作流需要的两个 secret：`ARCHIVE_DEPLOY_KEY`（归档仓的写权限 deploy key 私钥，只加在 ai-news-archive 上）和 `STATE_KEY`
（工作库的加密口令，随机 32 字节 base64；丢了只会丢失工作库，下一轮从空库重新采集，归档不受影响）。

### 服务器侧

```
~/ai-news-collector/            代码（无 git：用 scripts/server_update.sh 经 api.github.com 拉 tarball 覆盖，保留 data/ archive/ .env）
~/ai-news-archive/              私有归档仓的 git 克隆，server_publish.sh 往里追加 items/*.cn.jsonl 并 push
~/venvs/ai-news-collector/      venv（pip 走阿里云镜像）
~/ai-news-collector/.env        COLLECTOR_RUNNER=server  DATABASE_URL=sqlite:///data/collector.db  PROXY_URL=  GITHUB_TOKEN=<fine-grained PAT>
                                （server 侧 12 个源：量子位、智东西、InfoQ、钛媒体、爱范儿、极客公园、IT之家、少数派、雷峰网、开源中国、VentureBeat、MarkTechPost）
~/.ssh/ai-news-archive_ed25519  归档仓的 deploy key（写权限，私钥不离开服务器）；~/.ssh/config 里的别名 github-ai-news-archive 指向 ssh.github.com:443
~/.config/systemd/user/ai-news-collector.service   来自 deploy/systemd/，systemctl --user status ai-news-collector
crontab: 15 * * * * ~/ai-news-collector/scripts/server_publish.sh >> ~/logs/ai-news-publish.log 2>&1
         01 7 * * * ~/ai-news-collector/scripts/sync_digest.sh    >> ~/logs/ai-news-digest.log  2>&1
```

首次安装归档克隆（git 协议在这台机器上只有 SSH 走 443 端口能通）：

```bash
ssh-keygen -t ed25519 -N "" -f ~/.ssh/ai-news-archive_ed25519 -C "ai-news-collector server"
cat >> ~/.ssh/config <<'EOF'
Host github-ai-news-archive
    HostName ssh.github.com
    Port 443
    User git
    IdentityFile ~/.ssh/ai-news-archive_ed25519
    IdentitiesOnly yes
EOF
# 把 ~/.ssh/ai-news-archive_ed25519.pub 加到 ai-news-archive → Settings → Deploy keys（勾 Allow write access）
git clone github-ai-news-archive:xbbwa/ai-news-archive.git ~/ai-news-archive
git -C ~/ai-news-archive config user.name "ai-news-collector server"
git -C ~/ai-news-archive config user.email "ai-news-collector-server@users.noreply.github.com"
```

`GITHUB_TOKEN`（细粒度 PAT，只选 ai-news-collector 这一个仓库、Contents: Read and write）现在只用于 07:01 回传 pushed-history.jsonl
和 server_update.sh 拉 tarball 时提高限额；没配也不影响采集和全文归档。
体检：`~/venvs/ai-news-collector/bin/python scripts/check_sources.py`（自动只查 server 侧的源）。

## 采集器内部

```
config/sources.yaml  ── 信源清单（分层、轮询间隔、是否走代理、关键词过滤）
        │
scheduler ── run 模式：每个信源一个独立协程，按各自间隔轮询，失败指数退避；once 模式：全部拉一遍（Actions 用这个）
        │
fetchers ── rss（ETag / If-Modified-Since 条件请求）
         ── hackernews（Algolia 搜索 API）
         ── reddit（公开 Atom 订阅源 /r/<sub>/<listing>/.rss，无需账号；进程内串行、间隔 61s 以避开匿名限流）
         ── huggingface（Hub 公开 API，按组织监控模型发布；国内大模型厂商唯一可机读的一手渠道）
        │
pipeline ── 关键词/时效过滤 → URL 归一化 + sha256 去重 → 入库 → 并发抓正文（trafilatura，favor_recall 尽量保留原文）
         ── 正文下载遇到 403/503（Cloudflare）自动切换 Chrome 指纹客户端（curl_cffi），再失败切代理
        │
SQLite  ── items 表，自增 id 即消费游标；export_daily.py 按游标增量导出
        │
api ── GET /items?since_id=N&fetched_after=...  自建部署时供下游增量拉取（Actions 模式下不需要）
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

## 给 OpenClaw 的每日推送（国内服务器上的接法）

OpenClaw 用的是不开思考的 DeepSeek V4，让它读 90KB 原文、自己去重合并再翻译，效果差。所以把它不擅长的活全部放进脚本，
它只做翻译和排版：

```
Actions 每小时                         scripts/curate_digest.py → data 分支 digest/curated.md（≤20 条，~15KB）+ curated.json
   ├ 标题分词（英文词 / 中文二字词）做跨来源聚类：一件事被 5 家报道 = 1 条，"N 个来源"直接写在条目里
   ├ 打分排序：来源数 × 层级权重 + HN 分数 + HF likes + 发布类关键词 + 12h 内新鲜度
   ├ 过滤噪音：Reddit 自发帖、只有 Reddit/Product Hunt 单源的链接、没人点赞的 HF 上传、<80 分的 HN、TLDR 日报、GitHub Trending
   ├ 跨天去重：排除与 digest/pushed-history.jsonl（服务器回传的"已推送"）近 3 天相似的事件
   └ 多样性：每源最多 3 条，至少 4 条中文源
服务器 07:01   scripts/sync_digest.sh：下载 curated.md → daily-ai-news-curated.md，latest.md → daily-ai-news-summary.md（完整版留档）；
               mark_pushed.py 把这 20 条记为已推送，publish_archive.py 上传 pushed-history.jsonl 回 data 分支
OpenClaw 08:00 cron 任务 daily-ai-news-push：加载 skill daily-ai-news，只读 curated.md，翻译 + 固定模板 + 写 daily-push-history.md
OpenClaw 08:20 cron 任务 daily-push-healthcheck：history 日期不是今天就按 skill 补推
（两个任务的时间用 `openclaw cron edit <id> --cron "0 8 * * *" --tz Asia/Shanghai` 改；只给 --cron 会把 tz 字段清掉，要一起传）
```

- skill 文件：`deploy/openclaw/skills/daily-ai-news/SKILL.md`，部署到 `/mnt/data/openclaw-kb/openclawdata/skills/daily-ai-news/SKILL.md`
- 两个 cron 任务的提示词：`deploy/openclaw/cron/*.txt`（用 `openclaw cron edit <id> --message` 写入）
- 服务器 crontab：`01 7 * * * ~/ai-news-collector/scripts/sync_digest.sh >> ~/logs/ai-news-digest.log 2>&1`

OpenClaw 的 announce 投递**只发 agent 最后一段文字**（运行记录里的 `summary` 就是发出去的内容）。所以 skill 强制的顺序是：
静默读候选 → 静默写历史文件 → 最后一步才输出正文，且正文第一个字符必须是 📰（补推是 ⚠️）；任何"存档完成""以下是第二条"都会替代正文。
用 DeepSeek V4 Flash 实测：第一版 skill 发出去的是"存档完成。"，改成这个顺序后发出去的是完整正文（18 条、15 秒、1.9k 输出 token）。
测试补推的办法：把 `daily-push-history.md` 第一行日期改成昨天，`openclaw cron run <healthcheck-id>`，它会投递到用户私聊而不是群。

两个踩过的坑：工作区记忆里有一条用户偏好"长内容拆分多条"，OpenClaw 每次会话都会加载它，模型看到 18 条正文就往里插
（1/2）（2/2）把列表切断——skill 里必须显式声明这条偏好对定时推送不适用。`cron edit --light-context`（轻量启动上下文）
能去掉这类干扰，但实测 Flash 在轻量上下文下反而把推演文字写进最终回复、还跳过写文件步骤，所以两个任务都保持完整上下文；
健康检查任务的模型改成和正式推送相同的 `deepseek-v4-pro`（补推质量一致，正常时静默几乎不花钱）。

调参都在 workflow 里 `curate_digest.py` 的参数：`--max-items 20 --min-zh 4 --per-source-cap 3 --summary-chars 220 --exclude-source`。
泛科技源（带 `keywords` 的）的条目还要求**标题**本身命中 AI 关键词才进候选，否则 Axios/CNBC 的债券解读这类靠摘要过筛的会混进来。
实测一天 1232 条原始条目 → 1133 个事件 → 过滤 476 个噪音 → 20 条候选；排在前面的是 Claude 上 AWS、Gemini 视频理解、
NVIDIA 收购 HF、GPT-6 Astra 这类 3–4 家同时报道的事件。同一事件的英文公告和中文转载目前还是两条（不做跨语言聚类），skill 里让模型合并。

## 自建部署（可选，Docker）

不想依赖 GitHub Actions 时可以在自己的机器上常驻跑，compose 里有 `collector`（常驻调度）、`api`（:8000）、`rsshub`（:1200）、`redis` 四个服务：

```bash
cp .env.example .env      # PROXY_URL 填代理（如 http://host.docker.internal:7890），国内机器没有代理会有 13 个源被墙
docker compose up -d --build
docker compose exec api python scripts/check_sources.py    # 在容器里体检所有源（含 RSSHub 路由）
python3 scripts/daily_digest.py --api http://localhost:8000 --out digest.md
```

数据库 `./data/collector.db`（SQLite + WAL）必须放本地磁盘，不能放 NFS。国内服务器实际踩过的坑：`git clone` GitHub 会卡死
（改用 `git archive | ssh tar -x` 推过去）；Docker Hub 不通、镜像源列表里有死站时 `compose up` 会卡在拉镜像上毫无输出
（先 `docker pull docker.1panel.live/diygod/rsshub:latest` 再 `docker tag`）；pypi.org 一个请求 7 秒（`.env` 里设
`PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/`）；compose 调 buildx 会在写镜像时报 EOF（直接 `docker build -t ai-news-collector:latest .`）。

## 下游对接

**GitHub 模式（默认）**：全文读私有仓 `xbbwa/ai-news-archive` 的 `items/YYYY-MM-DD.jsonl`（每行一条，字段见下表，按 `id` 单调递增，
按天取增量，跨天用 `fetched_at` 或记住上次读到的 `id`；需要对该仓库有读权限的凭据）；摘要读本仓库公开 `data` 分支的 `digest/latest.md`
和 `digest/curated.md`，匿名 HTTPS 即可下载。

**自建 API 模式**：下游按游标增量拉取，`id` 单调递增，记住上次的 `next_since_id` 即可：

```
GET /items?since_id=0&limit=500
GET /items?since_id=0&fetched_after=2026-09-06T00:00:00Z   # 按抓取时间取一段
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

实测（2026-09-06）：GitHub Actions 首轮 71 个源、1144 条、3 分钟跑完，Reddit 两路 130 条、HF 模型发布国内 41 / 国外 72 条、HF 每日论文 28 条全部正常；只有 3 个源在美国 runner 上失败——VentureBeat（对数据中心 IP 返回 429）、Import AI（substack.com 对数据中心 IP 返回 403）、36氪 AI 频道（从海外访问 36kr 超时，快讯正常）；开源中国的 feed 能拉但正文页拒绝海外 IP。对比：国内服务器无代理时 73 个源里 18 个失败（Hugging Face、Reddit、Google Research / Cloud、Mistral、NYT、FT、Bloomberg、Guardian、Axios 全被墙），这是把采集搬到 GitHub 的直接原因。

采集本身**不需要任何账号或凭据**：所有信源都走公开接口，HTTP API 也不做鉴权。仅有的凭据都是往 GitHub 写东西用的：
归档仓的两把 deploy key（Actions 一把、服务器一把）、工作库加密口令 `STATE_KEY`，以及服务器回传 pushed-history 用的细粒度 PAT。

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
