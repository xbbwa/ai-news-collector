# ai-news-collector · data 分支

由 GitHub Actions（`main` 分支的 `.github/workflows/collect.yml`）每小时自动提交，**不要手工编辑**。

这个分支只放**摘要**（标题、短摘要、链接）。文章全文在私有仓库 [xbbwa/ai-news-archive](https://github.com/xbbwa/ai-news-archive) 的
`items/YYYY-MM-DD.jsonl` 里，那是第三方文章的正文，不能公开再分发，所以不在这里。

| 路径 | 内容 |
| --- | --- |
| `digest/latest.md` | 最近 24 小时的 Markdown 摘要（每源最多 3 条，摘要 300 字），完整版留档；每小时覆盖 |
| `digest/curated.md` / `curated.json` | 跨来源聚类、排序、去噪后的 ≤20 条候选，给 OpenClaw 推送用；每小时覆盖 |
| `digest/pushed-history.jsonl` | 服务器每天拉取后回传的"已推送"记录，用于跨天去重 |

下载（匿名 HTTPS 即可）：

```
https://raw.githubusercontent.com/xbbwa/ai-news-collector/data/digest/latest.md
https://raw.githubusercontent.com/xbbwa/ai-news-collector/data/digest/curated.md
```

备用：`https://api.github.com/repos/xbbwa/ai-news-collector/contents/digest/latest.md?ref=data`（请求头 `Accept: application/vnd.github.raw`）。

采集器的 SQLite 工作库（加密）和导出游标存放在名为 `state` 的 Release 资产里，同样由 workflow 自动维护。
