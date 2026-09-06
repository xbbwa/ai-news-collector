---
name: daily-ai-news
description: "Daily AI News 中文推送：读取已由脚本筛选排序好的候选清单 daily-ai-news-curated.md，翻译成中文并按固定模板输出到飞书。定时任务 daily-ai-news-push / daily-push-healthcheck 触发，或用户提到「AI 新闻」「AI 日报」「今日 AI」时加载。"
---

# Daily AI News 推送

## 你只做两件事：翻译、排版

候选清单已经由脚本完成了跨来源合并、跨天去重、噪音过滤和按重要程度排序。
你**不要**再做筛选、去重、排序，**不要**联网，**不要**读其他文件（尤其不要读 daily-ai-news-summary.md，那是给人看的完整版）。

## 输入

只读这一个文件：`/mnt/data/openclaw-kb/openclawdata/daily-ai-news-curated.md`

- 第 2 行是「生成时间」。如果生成时间距现在超过 30 小时、文件不存在、或条目为 0：只输出一行
  `⚠️ Daily AI News 今日无可用数据（原因：xxx）` 然后结束，不要编造内容。
- 每条候选包含：序号、原文标题、语言、来源（N 个来源）、热度、摘要、发布时间、链接、同事件报道。
  「N 个来源」越大说明越多媒体同时报道，越重要；顺序已经按重要程度排好。

## 输出规则

1. 按候选顺序逐条输出，全部译成中文；语言为 zh 的条目直接润色标题，不改动事实。
2. 每条严格两行：
   `N. 【中文标题】`
   `   一句中文摘要（不超过 45 字）｜来源：A、B（共 N 家）`
3. 标题里的产品名、模型名、公司名保留原文，不翻译：GPT-6 Astra、Claude、Gemini 3.8 Flash、Hugging Face、NVIDIA、DeepSeek、Qwen 等。数字、金额、版本号照抄。
4. 摘要只能改写候选里的「摘要」和「同事件报道」两行，不得加入候选里没有的信息，不加评论、不加表情。
5. 两条候选如果明显是同一事件（例如同一次发布的公告和它的安全报告、同一新闻的中英文报道），合并成一条：要点用「；」分隔，来源合并去重。合并后总条数不少于 10 条。
6. 不带链接，不用 @all 或 @所有人，不用卡片，不用 Markdown 的 # 标题、表格、粗体。
7. 第一行固定为 `📰 Daily AI News · YYYY-MM-DD（共 N 条）`，日期取候选文件的生成日期，然后直接列条目。
8. **结尾不要有任何收尾语**（"任务完成""以上""推送已送达""存档完成"都会被当作正文发到群里）。
9. 一条消息最多 12 条新闻。超过时拆成多条消息发送，每条消息第一行标 `（1/2）`、`（2/2）`。

## 存档（08:30 的健康检查靠它判断今天是否推送成功）

输出推送正文后，把候选文件里全部条目的**原文标题**（不翻译、不改）覆盖写入
`/mnt/data/openclaw-kb/openclawdata/daily-push-history.md`，格式：

```
# Daily Push History — YYYY-MM-DD
## 今日已推送标题
- 原文标题 1
- 原文标题 2
```

日期用今天的北京日期。定时任务里无人可确认，这个固定文件直接写，不走确认流程。写完不要汇报。

## 示例

候选：

```
## 3. NVIDIA to Acquire Hugging Face
- 语言：en ｜ 来源：NVIDIA 博客、Ars Technica、New York Times — Technology（3 个来源） ｜ 热度：11.0
- 摘要：NVIDIA announced it will acquire Hugging Face for $12.9B and committed to keeping the platform open ...
```

输出：

```
3. 【NVIDIA 宣布 129 亿美元收购 Hugging Face】
   承诺交易后保持平台开放｜来源：NVIDIA 博客、Ars Technica、纽约时报（共 3 家）
```
