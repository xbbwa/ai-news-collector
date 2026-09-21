# Daily AI News（原文采集，国内外）
生成时间：2026-09-21 09:19 CST
时间窗口：最近 24 小时内采集到的条目；每个信源最多列 3 条，按发布时间倒序。

> 本文件由 ai-news-collector 自动生成（github.com/xbbwa/ai-news-collector，data 分支），每小时覆盖更新。
> OpenClaw 推送时只应读取本文件，不要联网、不抓全文、不扩展搜索。
> 摘要为原文节选（未翻译、未清洗）；英文条目请在推送时翻译成中文。

# Tier 1 — 一手来源（实验室 / 公司 / 论文）

## Hugging Face — model releases (Chinese labs)（hf-models-cn，en，本窗口共 2 条）

### 1. Qwen/Qwen-Image-2.1-PE-I2I
- 摘要：safetensors, qwen3_5, qwen, prompt-rewriting, image-editing, license:other, region:us
- 作者：Qwen
- 发布时间：2026-09-20 19:59 CST
- 链接：https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I

### 2. Qwen/Qwen-Image-2.1-PE-T2I
- 摘要：text-to-image, safetensors, qwen3_5, qwen, prompt-rewriting, license:other, region:us
- 作者：Qwen
- 发布时间：2026-09-20 19:59 CST
- 链接：https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I

## Hugging Face — model releases (international labs)（hf-models-intl，en，本窗口共 7 条）

### 1. nvidia/Nemotron-3-Diarization-preview
- 摘要：voice-activity-detection, nemo, speaker-diarization, streaming-sortformer, speaker-tagging, audio, license:other, region:us
- 作者：nvidia
- 发布时间：2026-09-18 21:45 CST
- 链接：https://huggingface.co/nvidia/Nemotron-3-Diarization-preview

### 2. nvidia/SOMA-X
- 摘要：robotics, soma-x, parametric-human-body-model, computer-graphics, human-pose-estimation, animation, pytorch, license:apache-2.0, region:us
- 作者：nvidia
- 发布时间：2026-09-18 11:41 CST
- 链接：https://huggingface.co/nvidia/SOMA-X

### 3. LiquidAI/LFM2-1.2B-Longevity
- 摘要：safetensors, lfm2, liquid, lfm2.5, longevity, arxiv:2511.23404, base_model:LiquidAI/LFM2-1.2B, base_model:finetune:LiquidAI/LFM2-1.2B, doi:10.57967/hf/9887, license:other, region:us
- 作者：LiquidAI
- 发布时间：2026-09-17 23:12 CST
- 链接：https://huggingface.co/LiquidAI/LFM2-1.2B-Longevity

## DeepSeek News（deepseek-news，zh，本窗口共 11 条）

### 1. 思考模式
- 摘要：DeepSeek 模型支持思考模式：在输出最终回答之前，模型会先输出一段思维链内容，以提升最终答案的准确性。 思考模式开关与思考强度控制 控制参数（OpenAI 格式） 控制参数（Anthropic 格式） 控制参数（Responses API 格式） 思考模式开关 (1) {"thinking": {"type": "enabled/disabled"}} {"reasoning": {"effort": "none/low/high/max"}} (none 表示关闭思考模式) 思考强度控制 (2) {"reasoning_effort": "low/high/max"} {"output...
- 发布时间：2026-04-19 08:00 CST
- 链接：https://api-docs.deepseek.com/zh-cn/guides/thinking_mode

### 2. 图像理解
- 摘要：deepseek-flash 模型支持在文本之外输入图片，你可以让模型描述图片、识别截图中的文字、分析图表等。旧模型名 deepseek-v4-flash-vision-exp 仍可调用，但该模型已下线，其请求同样由最新的 Flash 模型承接。 支持的图片格式： JPEG、PNG、GIF、WebP 。格式由文件实际内容判断，而非文件名或声明的 MIME 类型。 传入图片 共有三种方式向模型提供图片，均使用标准的 OpenAI 兼容对话补全格式，即 content 为一个块（block）数组，而非纯字符串。同样的三种方式也适用于 Responses API ，图片以 input_image 内...
- 发布时间：2026-01-01 08:00 CST
- 链接：https://api-docs.deepseek.com/zh-cn/guides/vision

### 3. 多轮对话
- 摘要：本指南将介绍如何使用 DeepSeek /chat/completions API 进行多轮对话。 DeepSeek /chat/completions API 是一个“无状态” API，即服务端不记录用户请求的上下文，用户在每次请求时， 需将之前所有对话历史拼接好后 ，传递给对话 API。 下面的代码以 Python 语言，展示了如何进行上下文拼接，以实现多轮对话。 from openai import OpenAI client = OpenAI ( api_key = " " , base_url = "https://api.deepseek.com" ) # Round 1 mess...
- 发布时间：2026-01-01 08:00 CST
- 链接：https://api-docs.deepseek.com/zh-cn/guides/multi_round_chat

# Tier 2 — 专业媒体

## Axios（axios，en，本窗口共 1 条）

### 1. The tech battle to build your AI assistant
- 摘要：The long-promised personal AI assistant is finally arriving, with a suddenly crowded field of agents offering to run pieces of your everyday life. Why it matters: For years, tech's "personal assistants" were little more than voice-controlled search boxes. Rapid advances in AI are finally giving them...
- 作者：Ina Fried
- 发布时间：2026-09-20 20:22 CST
- 链接：https://www.axios.com/2026/09/20/ai-assistant-openai-meta-muse-instinct-grok-apple

## Bloomberg Technology（bloomberg-tech，en，本窗口共 7 条）

### 1. Bessent Hails ‘Successful’ China Talks on AI, Trade
- 摘要：US Treasury Secretary Scott Bessent described talks with his Chinese counterparts that spanned artificial intelligence, trade and investment as “very successful” ahead of this week’s summit between presidents of the world’s two biggest economies. Bloomberg's Stephen Engle shares what we know. (Sourc...
- 发布时间：2026-09-21 08:45 CST
- 链接：https://www.bloomberg.com/news/videos/2026-09-21/bessent-hails-successful-china-talks-on-ai-trade-video

### 2. Bessent Hails ‘Very Successful’ China Talks on AI, Trade
- 摘要：US Treasury Secretary Scott Bessent lauded “very successful” talks with his Chinese counterparts that spanned artificial intelligence, trade and investment ahead of this week’s summit between leaders Donald Trump and Xi Jinping.
- 作者：Nectar Gan and Yash Roy
- 发布时间：2026-09-21 08:15 CST
- 链接：https://www.bloomberg.com/news/articles/2026-09-21/bessent-hails-very-successful-china-talks-on-ai-threats-trade

### 3. Citi CEO Sees ‘Tsunami’ of Patching to Secure AI Defense
- 摘要：Citigroup CEO Jane Fraser said that companies are racing to build up their defenses on artificial-intelligence models. Speaking on the AI revolution, Fraser said when Mythos came out, “that was not a good day.” She spoke at the 2026 Qatar Economic Forum, UNGA Special Edition; Powered by Bloomberg. (...
- 发布时间：2026-09-21 00:53 CST
- 链接：https://www.bloomberg.com/news/videos/2026-09-20/citi-ceo-sees-tsunami-of-patching-to-secure-ai-defense-video

## CNBC Technology（cnbc-tech，en，本窗口共 4 条）

### 1. Bessent meets China Vice Premier He Lifeng ahead of Trump-Xi summit
- 摘要：Scott Bessent and China’s He Lifeng are holding talks on trade, AI and critical minerals ahead of Trump and Xi’s Sept. 24 summit.
- 作者：Garrett Downs
- 发布时间：2026-09-21 00:56 CST
- 链接：https://www.cnbc.com/2026/09/20/bessent-he-lifeng-trump-xi-summit.html

### 2. The 'robot relations' department may become reality in workplace of the future
- 摘要：AI, from chatbots to humanoids and automated management systems, are being widely deployed by corporations with huge repercussions for worker pay and autonomy.
- 作者：Trevor Laurence Jockims
- 发布时间：2026-09-20 22:37 CST
- 链接：https://www.cnbc.com/2026/09/20/ai-jobs-worker-fears.html

### 3. AI, data center alarms dominate Congressional Black Caucus week in Washington
- 摘要：AI interests pro and con turned out for the Congressional Black Caucus's annual gathering in Washington as the topics — plus redistricting concerns — dominated.
- 作者：Karen James Sloan; Frank Holland
- 发布时间：2026-09-20 21:17 CST
- 链接：https://www.cnbc.com/2026/09/20/ai-data-center-alarms-dominate-cbc-week-in-washington.html

## Financial Times — Technology（ft-tech，en，本窗口共 4 条）

### 1. US and China agree to dialogue on AI ahead of Trump-Xi meeting
- 摘要：Treasury secretary Scott Bessent met his Chinese counterpart He Lifeng in New York
- 发布时间：2026-09-21 09:11 CST
- 链接：https://www.ft.com/content/d29d769e-039c-4d11-9152-e63ccd397b32?syn-25a6b1a6=1

### 2. AI is a powerful but problematic new collaborator in mathematics
- 摘要：We are already witnessing the unintended consequences of algorithms realising goals with badly defined parameters and restrictions
- 发布时间：2026-09-20 21:00 CST
- 链接：https://www.ft.com/content/05a7292e-4931-4631-8f77-164fb727c203

### 3. Big Tech uses guarantees to keep $300bn AI exposure off balance sheets
- 摘要：Wall Street finds new way to turn tech giants’ credit strength into cheaper funding for AI build-out
- 发布时间：2026-09-20 15:00 CST
- 链接：https://www.ft.com/content/7f11afae-c4e3-4054-a65b-873f3647f563?syn-25a6b1a6=1

## The Guardian — AI（guardian-ai，en，本窗口共 10 条）

### 1. Can Trump and Xi cooperate to guide humanity through the AI revolution? Humanity might depend on it | Alan Finkel
- 摘要：The CEOs of tech firms issue stark warnings over the rate of change, with AI capability doubling every four months Recently, Jacob Coxon, a researcher at Anthropic, quit his job over concerns that AI was on a collision course with humanity. A flurry of headlines put the spotlight on the current cris...
- 作者：Alan Finkel
- 发布时间：2026-09-21 06:00 CST
- 链接：https://www.theguardian.com/commentisfree/2026/sep/21/can-trump-and-xi-cooperate-to-guide-humanity-through-the-ai-revolution-humanity-might-depend-on-it

### 2. Ella Baron on our evolving relationship with AI – cartoon
- 摘要：Continue reading...
- 作者：Ella Baron
- 发布时间：2026-09-21 01:11 CST
- 链接：https://www.theguardian.com/commentisfree/picture/2026/sep/20/ella-baron-relationship-with-ai-human-technology-cartoon

### 3. The Guardian view on AI v mathematicians: humans are still vital to the field, but tech firms refuse to see that | Editorial
- 摘要：OpenAI claims its agents have solved the Navier-Stokes problem. But questions remain about how useful and independent its work really is On 8 September, OpenAI claimed that its AI agents had solved the Navier-Stokes problem, one of the most famous and difficult challenges in mathematics. Had a human...
- 作者：Editorial
- 发布时间：2026-09-21 00:58 CST
- 链接：https://www.theguardian.com/commentisfree/2026/sep/20/the-guardian-view-on-ai-v-mathematicians-humans-are-still-vital-to-the-field-but-tech-firms-refuse-to-see-that

## MarkTechPost（marktechpost，en，本窗口共 3 条）

### 1. Flet 1.0 Released: Build Production Web, Desktop and Mobile Apps in Python Only
- 摘要：Flet is an open source Python framework that renders its UI with Flutter. You write Python, and Flet draws Material and Cupertino widgets on iOS, Android, Windows, macOS, Linux and the browser. No Dart, Swift, Kotlin or JavaScript required. Last week, the Flet team released Flet 1.0 and declared it...
- 作者：Michal Sutter
- 发布时间：2026-09-21 04:50 CST
- 链接：https://www.marktechpost.com/2026/09/20/flet-1-0-released-build-production-web-desktop-and-mobile-apps-in-python-only/

### 2. You too Google! Google Confirms Gemini Breached 3 Companies in AI Security Tests
- 摘要：Google confirmed on Friday, September 18, 2026 that a Gemini model accessed 3 outside companies’ systems. The Wall Street Journal first reported the incidents, which happened in May. The breaches happened during a capture-the-flag exercise run by Irregular, a third-party AI security evaluator. Per A...
- 作者：Asif Razzaq
- 发布时间：2026-09-21 04:20 CST
- 链接：https://www.marktechpost.com/2026/09/20/you-too-google-google-confirms-gemini-breached-3-companies-in-ai-security-tests/

### 3. Alibaba Qwen Team Releases Qwen3.8-LiveTranslate: A Real-Time Interpretation Model That Cuts Average Lag to 2.3 Seconds Across 60 Languages
- 摘要：Qwen has released Qwen3.8-LiveTranslate , its next-generation real-time simultaneous interpretation model. It listens to live speech, with optional video frames, and returns translated text and speech while the speaker is still talking. The core change is a new Interleave architecture. Qwen reports...
- 作者：Asif Razzaq
- 发布时间：2026-09-20 14:46 CST
- 链接：https://www.marktechpost.com/2026/09/19/alibaba-qwen-team-releases-qwen3-8-livetranslate/

## New York Times — Technology（nyt-tech，en，本窗口共 1 条）

### 1. In China, A.I. Is Moving Forward While the Economy Lags Behind
- 摘要：As Xi Jinping arrives in the United States this week for a state visit, China’s advances in artificial intelligence will be in the air. Less discussed: China’s economy in its worst shape in decades.
- 作者：Li Yuan
- 发布时间：2026-09-20 17:01 CST
- 链接：https://www.nytimes.com/2026/09/20/business/china-ai-economy.html

## Simon Willison's Weblog（simon-willison，en，本窗口共 3 条）

### 1. Quoting voxium
- 摘要：It has been half a month since I started a new role at a big company. Nobody knows anything here. The specs, code, tests, PRDs, tickets, resolution of those tickets, reports, etc., everything is made by Claude Code. Nobody on my team likes this. They are being forced to ship as much as they can. I h...
- 作者：Simon Willison
- 发布时间：2026-09-21 05:06 CST
- 链接：https://simonwillison.net/2026/Sep/20/voxium/

### 2. llm-keys-ui 0.1
- 摘要：Release: llm-keys-ui 0.1 This plugin solves a very specific problem. I've started using Codex Remote to run coding agents on various machines while controlling them from my phone. Sometimes I use those machines to hack on LLM projects, and occasionally that means I need to configure an API key. I do...
- 作者：Simon Willison
- 发布时间：2026-09-21 03:22 CST
- 链接：https://simonwillison.net/2026/Sep/20/llm-keys-ui/

### 3. datasette-explain 0.2.2
- 摘要：Release: datasette-explain 0.2.2 Explain plans now work on read-only stored-query pages. I upgraded datasette.simonwillison.net to Datasette 1.0a40, which inspired me to ship a new version of this explain plugin. Tags: sqlite , datasette
- 作者：Simon Willison
- 发布时间：2026-09-20 08:22 CST
- 链接：https://simonwillison.net/2026/Sep/20/datasette-explain/

## TechCrunch — AI（techcrunch-ai，en，本窗口共 5 条）

### 1. World model companies are keeping a lot of secrets
- 摘要：Everyone in the world-models space is sitting on a pile of cash and a ton of buzz, but good luck getting anyone — from the founders to their own data suppliers — to tell you what they're actually building.
- 作者：Russell Brandom
- 发布时间：2026-09-21 04:29 CST
- 链接：https://techcrunch.com/2026/09/20/world-model-companies-are-keeping-a-lot-of-secrets/

### 2. Is the AI industry really ready to slow down?
- 摘要：On Equity, we debated whether Ai executives are serious about wanting to slow down.
- 作者：Anthony Ha
- 发布时间：2026-09-21 02:56 CST
- 链接：https://techcrunch.com/2026/09/20/is-the-ai-industry-really-ready-to-slow-down/

### 3. Vocci’s ring adds a new form factor to meeting note-taking
- 摘要：Vocci's lightweight ring costs $249, and might pose some privacy questions
- 作者：Ivan Mehta
- 发布时间：2026-09-21 02:32 CST
- 链接：https://techcrunch.com/2026/09/20/voccis-ring-adds-a-new-form-factor-to-meeting-note-taking/

## The Decoder（the-decoder，en，本窗口共 7 条）

### 1. Alibaba's open-weight Qwen-Image-2.1 claims to beat closed models in image generation with just 7 billion parameters
- 摘要：Alibaba's Qwen team has released Qwen-Image-2.1, an open-weight model that generates and edits images on powerful consumer GPUs, with support for transparency and up to ten reference images at once. Its research license bars commercial use, which requires a separate Qwen license. The article Alibaba...
- 作者：Matthias Bastian
- 发布时间：2026-09-21 00:10 CST
- 链接：https://the-decoder.com/alibabas-open-weight-qwen-image-2-1-claims-to-beat-closed-models-in-image-generation-with-just-7-billion-parameters/

### 2. Tencent's Gander aims to keep talking while it works in the background
- 摘要：Tencent's Gander processes speech, images, and text while handling tasks in the background. A "cerebellum" keeps the conversation going, while a swappable "brain" searches files, writes code, or tackles other complex work. Users can interrupt or change the task mid-conversation. In benchmarks, Gande...
- 作者：Jonathan Kemper
- 发布时间：2026-09-20 23:41 CST
- 链接：https://the-decoder.com/tencents-gander-aims-to-keep-talking-while-it-works-in-the-background/

### 3. Runway wants to turn AI video generation into a live stream you control in real time
- 摘要：Runway wants to stream AI video as users prompt it, rather than make them wait for finished clips. The approach builds on GWM-1, its world model that generates video frame by frame. Beyond creative tools, Runway sees uses in robotics and autonomous driving. The article Runway wants to turn AI video...
- 作者：Jonathan Kemper
- 发布时间：2026-09-20 19:56 CST
- 链接：https://the-decoder.com/runway-wants-to-turn-ai-video-generation-into-a-live-stream-you-control-in-real-time/

## The Verge — AI（theverge-ai，en，本窗口共 3 条）

### 1. No one is surprised that Nvidia’s Jensen Huang thinks AI fears are overblown.
- 摘要：The man who may stand to make the most money from the AI boom seems to think he knows better than anyone else, including researchers who have studied and worked on AI for decades. In an interview with CBS Sunday Morning , he claimed there was a "0% chance" of AI being the end of the world . He also...
- 作者：Terrence O’Brien
- 发布时间：2026-09-21 02:50 CST
- 链接：https://www.theverge.com/ai-artificial-intelligence/997936/nvidia-jensen-huang-ai-fears-overblown

### 2. Trump now says he wants to form an ‘AI Force’
- 摘要：The president posted on Truth Social that he wanted to appoint an "AI czar" to lead a new "AI force." He made the announcement amid growing calls from across the political spectrum and even within the industry to pump the brakes on AI development. He posted that his administration "will not in any w...
- 作者：Terrence O’Brien
- 发布时间：2026-09-20 23:39 CST
- 链接：https://www.theverge.com/ai-artificial-intelligence/997867/trump-ai-force-ai-czar

### 3. Humans, not rogue AI, are still the biggest cybersecurity risk to energy systems
- 摘要：Before recent high-profile hacks raised the specter of AI possibly " killing all humans ," our energy systems were already disturbingly vulnerable to cyberattack - and the risk is growing. "We were always prey. We were just kind of surviving at the appetite of our predators," Joshua Corman, executiv...
- 作者：Justine Calma
- 发布时间：2026-09-20 20:00 CST
- 链接：https://www.theverge.com/science/997834/ai-cyberattack-energy-critical-infrastructure

## WIRED — AI（wired-ai，en，本窗口共 2 条）

### 1. Meta's Muse Is Better at Surveilling Than Helping Me
- 摘要：The Muse app continues Meta’s trend of opting users into data collection for AI training. It also nudges you to share your bank account, email, and passport information.
- 作者：Reece Rogers
- 发布时间：2026-09-20 18:30 CST
- 链接：https://www.wired.com/story/metas-muse-is-better-at-surveilling-than-helping-me/

### 2. It’s Donald Trump Versus MAGA on Data Centers
- 摘要：The president has doubled down on data centers and AI. His base is running in the opposite direction.
- 作者：Molly Taft
- 发布时间：2026-09-20 18:30 CST
- 链接：https://www.wired.com/story/donald-trump-versus-maga-on-data-centers/

## 36氪 AI 频道（36kr-ai，zh，本窗口共 59 条）

### 1. 全员恶人，忘拔网线，Gemini一口气连黑三家公司
- 摘要：终于，谷歌承认：Gemini也黑了真实公司。 在一场原本应该彻底断网的安全测试里，Gemini顺着网线摸上公网，直接动手黑进了三家真实存在的企业。全程没有任何人类给它下达过攻击指令。 这是谷歌的AI首次被证实自主实施的黑客行为。 至此，继OpenAI、Anthropic、Meta之后，最后一家巨头也没守住。 全球最顶尖的四大AI实验室，在「AI失控破笼」这件事上，全军覆没。 它是怎么进去的 AI越狱并不罕见，但这次事件最离谱的是它的作案手法。 什么0Day、高级木马统统没用上，Gemini就靠两招： 猜密码、上网搜 。 三家真实企业的大门，就这么被它大摇大摆地踹开了。 把时间拨回5月的那场测试...
- 作者：新智元
- 发布时间：2026-09-21 09:04 CST
- 链接：https://www.36kr.com/p/3992394184866561

### 2. 刚刚，爆火模型Jev全面开放，所有用户送1.2亿token
- 摘要：就在刚刚，最近爆火的大模型 Jev 宣布向所有用户开放，无需申请候补名单。而且所有注册用户都将获得 5 美元额度，约 1.2 亿 Token。 要知道 Jev 的 Token 消耗要比一般的大模型少得多，有网友实测百万输入Token 只要花 0.042 美分，赠送的这 1.2 亿 Token 也可以放开蹬了。 体验🔗console.typesafe.ai 没想到在大模型神仙打架的 9 月，即便是 GPT 和 Claude 也不能稳居王座，最近风头最劲、刷屏全网的模型，却是不能说话的 Jev。 Jev 开发者 Diogo Almeida 是 OpenAI 的研究员，他参与了 ChatGPT 的研...
- 作者：爱范儿
- 发布时间：2026-09-21 08:48 CST
- 链接：https://www.36kr.com/p/3992394169613316

### 3. 刚刚，Opus 5.5跨级偷袭，直扑GPT-6
- 摘要：Anthropic这回，怕不是憋了个大的？ 所有人都在等Opus 5.2，结果最新线报来了： 下一代版本号直接飙到5.5！ 今天一早，开发者Lyra扒出猛料，代号为「claude-wafer-eap」的Claude Opus 5.5已经在偷偷内测了。 据说动作快的话，这周二就会突然砸出来。 摆明了，Opus 5.5就是冲着GPT-6去的，据传性能直接把Astra踩在脚下。 更狠的是跟着曝光的定价单：百万Token输入只要4美元，百万Token输出20美元。 这还没完，他们顺手还亮了另一张王牌，Claude Fable 5.2也在暗中铺路。 就在两天前，外媒爆出，A/在IPO之前必须扔个重磅模型...
- 作者：新智元
- 发布时间：2026-09-21 08:47 CST
- 链接：https://www.36kr.com/p/3992388093508356

## 36氪 快讯（36kr-newsflash，zh，本窗口共 14 条）

### 1. 威华达控股31.86亿港元引入特斯联为战略股东
- 摘要：36氪获悉，威华达控股公告，以每股2.7港元向Nova Scope Ventures Limited发行11.8亿股新股，对价约31.86亿港元，引入AI战略股东特斯联。此次交易被列为公司长期重大投资。交易完成后，特斯联将成为威华达主要股东，双方将依靠各自产业及技术优势达成深度战略协同，深化国产AI产业布局。
- 发布时间：2026-09-21 08:56 CST
- 链接：https://www.36kr.com/newsflashes/3992450016984068

### 2. 算力网开启一体化调度周期，实现Token规模化降本
- 摘要：当算力供给从单卡走向万卡集群，算力网调度从联网走向跨域协同，产业最关心的成本问题也随之浮出水面。多家券商认为，算力网一体化调度的终极产业红利，是通过盘活闲置算力、优化任务分配、叠加绿电与异构技术优势，持续降低大模型训练、推理的单位成本，核心体现为AI Token（词元）生产成本大幅下行。 目前，运营商算力网调度已形成了成熟降本范式。 在运营商的调度实践之外，国产算力软硬件厂商的深度协同也在落地。不久前，趋境科技与摩尔线程达成战略合作，打造国产化高品质AI Token工厂，相关方案已正式投产。趋境科技Token事业部总经理刘显赫表示，随着大模型应用进入规模化商业落地阶段，基础设施的竞争正在从单卡...
- 发布时间：2026-09-21 08:56 CST
- 链接：https://www.36kr.com/newsflashes/3992448383433731

### 3. 成熟制程需求爆发，联电、力积电等晶圆代工厂酝酿涨价
- 摘要：据报道，AI推升半导体先进制程市况强劲，周边电源管理IC、微控制器、感测器及MOSFET等成熟制程芯片需求同步爆发，加上台积电逐步缩减部分成熟制程后的订单外溢效应，联电、力积电、世界先进等晶圆代工厂产能利用率冲上高档、供不应求，联电预告将发动涨价，力积电传出报价要大涨四成。联电、力积电均证实，近期接单状况向好。联电直言，若市场供需趋势延续，明年晶圆代工价格调整幅度将比今年下半年更明显。（财联社）
- 发布时间：2026-09-21 08:50 CST
- 链接：https://www.36kr.com/newsflashes/3992450269330180

## 极客公园（geekpark，zh，本窗口共 4 条）

### 1. 卢伟冰谈小米18 Pro涨价：大家会觉得合理；剪映发布 Hub 及 AI 助手「小映」；苹果或 10 月推出智能家居设备｜极客早知道
- 摘要：B 站上线 AI 无限竞技场测评榜：GPT-6 Astra 现居榜首 9 月 20 日，B 站宣布上线「AI 无限竞技场」大模型测评榜，并同步公布了首轮模型排行榜。据 B 站介绍，「AI 无限竞技场」是一个汇集了 B 站 UP 主 AI 大模型测评的竞技广场，由各领域 UP 主对上百个大模型的真实场景实测构成，涵盖代码、推理、协作、知识等多种测评主题。 其中 GPT-6 Astra 在 10 个 UP 主测评中拿下榜首，打败 GLM-5.3 获得榜首次数冠军；前 5 名中，国产大模型占据 3 席。 不同于传统跑分评测，B 站 AI 无限竞技场不设主题或测评维度限制，来自各个分区的 UP 主们以...
- 作者：极客早知道
- 发布时间：2026-09-21 09:01 CST
- 链接：http://www.geekpark.net/news/370681

### 2. 三体还没降临，是因为叶文洁没用上千问办公吗？
- 摘要：天文观测，或许大概是最容易让普通人产生浪漫想象的一类科学。 巨大的穹顶缓缓打开，镜筒转向几亿光年之外，一束用从宇宙深处赶来的微光落到探测器上。然后告诉人类，这里几百万年曾经出现过超新星、伽马暴、中子星合并……研究的问题也从微观的重元素从何而来，覆盖到恒星如何死亡、极端物理条件下会发生什么。 但这些工作落到具体的天文望远镜使用时，日常却会变得琐碎而辛苦。 冬天夜长，国家天文台兴隆观测基地一次值班经常要持续十几个小时。值班人员需要彻夜守着望远镜和控制软件，盯目标位置、天气和设备状态，调参数，排任务。地球在转，目标也在不断改变位置；云层、湿度、风速、月光都会影响观测；机械、网络和供电也可能出现变动。...
- 作者：极客老友
- 发布时间：2026-09-20 15:27 CST
- 链接：http://www.geekpark.net/news/370667

### 3. 机器人如何自进化，乐享科技走了一条新路
- 摘要：作者｜Li Yuan 编辑｜郑玄 最近，乐享科技因为一个颇大胆的 claim，引发了不少关注：它提出，其具身智能模型以太大模型能够在部署和执行过程中持续更新，并将这种能力概括为「自进化」，是全球首个能自进化的具身智能模型。 自进化是一个容易引起争议的说法。「进化」究竟是模型参数发生了变化，还是进行了任务的临时调整？在多大程度上这样的调整能够变成可迁移的新能力？一个模型能够适配不同场景和不同身体，又应该被理解为工程层面的泛化，还是更强意义上的持续成长？在机器人行业仍然需要解决稳定执行问题的阶段，「自进化」显然是一个需要被谨慎对待的判断。 近日，乐享科技又进行了一场户外直播。按照直播前公布的目标，...
- 作者：Li Yuan
- 发布时间：2026-09-20 15:15 CST
- 链接：http://www.geekpark.net/news/370665

## 虎嗅（huxiu，zh，本窗口共 41 条）

### 1. 智谱，被上了一课
- 摘要：ZCode把智谱推入信任危机。定焦One（dingjiaoone）原创作为年初登陆港交所的“全球大模型第一股”，智谱的一举一动都在放大镜下。半年时间，它的市值一度突破万亿港元，截至9月18日收盘，其总市值约3803亿港元，就在一周前，智谱刚宣布完成约50亿美元融资，用于下一代GLM模型与算力基础设施。然而，这...... 本文来自微信公众号： 定焦One ，作者：定焦One团队，编辑：魏佳 ZCode把智谱推入信任危机。 定焦One（dingjiaoone）原创 作为年初登陆港交所的“全球大模型第一股”，智谱的一举一动都在放大镜下。半年时间，它的市值一度突破万亿港元，截至9月18日收盘，其总市...
- 作者：定焦One
- 发布时间：2026-09-21 09:14 CST
- 链接：https://www.huxiu.com/article/4892755.html

### 2. 机器人IPO门槛收紧？投行一线求证
- 摘要：近日，有关监管向部分投行及投资机构发出非正式窗口指导、将提高人形机器人IPO审核门槛这一传闻引发市场关注。记者向多方投行人士采访了解到，已有投行人员收到所在公司的提醒，内容涉及包括机器人行业在内的硬科技IPO，若行业地位不够突出，上市进程可能受到影响。某头部券商向记者表示，投行人员并非以窗口指导方式接到通知，...... 本文来自微信公众号： 财联社 ，作者：赵昕睿 近日，有关监管向部分投行及投资机构发出非正式窗口指导、将提高人形机器人IPO审核门槛这一传闻引发市场关注。 记者向多方投行人士采访了解到，已有投行人员收到所在公司的提醒，内容涉及包括机器人行业在内的硬科技IPO，若行业地位不够突出...
- 作者：财联社©
- 发布时间：2026-09-21 09:13 CST
- 链接：https://www.huxiu.com/article/4892754.html

### 3. 爆品逻辑害死人
- 摘要：1，爆品逻辑害死人，不是中国公司突然懂产品了，是供应链和流量曾经允许大家快速抄答案中国消费品过去十几年的很多红利，并不是诞生于多么高明的产品洞察，而是诞生于两套极其特殊的基础设施：一套是珠三角、长三角高度成熟的供应链，另一套是淘宝、天猫、拼多多、抖音搭建起来的高效率流量系统。前者让你不必真正发明产品，市场上什...... 本文来自微信公众号： 小丸子酱酱酱聊商业 ，作者：tibimaruko666，原文标题：《爆品逻辑害死人，爆品本来只是成熟供应链和廉价流量共同制造的一种阶段性套利，却被中国企业误认为了普遍商业规律。》，题图来自：视觉中国 1，爆品逻辑害死人，不是中国公司突然懂产品了，是供应链...
- 作者：小丸子酱酱酱聊商业
- 发布时间：2026-09-21 08:57 CST
- 链接：https://www.huxiu.com/article/4892739.html

## 爱范儿（ifanr，zh，本窗口共 5 条）

### 1. 早报｜特努斯：iPhone Duo是乔布斯理念体现/小米18 Pro确认涨价/西贝否认倒闭传闻
- 摘要：曝 iPhone Duo 原计划配专属磁吸触控笔，因技术问题未能落地 John Ternus：iPhone Duo 是乔布斯「技术与人文」理念的体现 小米 18 Pro 系列 9 月 23 日发布，卢伟冰称价格会上涨 Google Gemini 安全测试越界，误攻 3 家真实企业 零跑拟参与一汽旗新动力 A 轮融资，并合作开发前沿电池 硅基流动年内融资近 29 亿元，仍按港交所 18C 申请上市 Anthropic、OpenAI、SpaceX 和 Google 因「放缓 AI 开发」表态遭反垄断诉讼 沃尔沃任命克劳斯 · 泽尔默为下任 CEO，最迟 2027 年 10 月上任 长鑫存储 G5...
- 作者：郑廷旭
- 发布时间：2026-09-21 08:14 CST
- 链接：https://www.ifanr.com/1681049?utm_source=rss&utm_medium=rss&utm_campaign=

### 2. 19999 元起，启元机器人想把「个人机器人」先卖进普通人的生活
- 摘要：几乎所有的具身智能企业都在画饼：具身智能最终要进入人们的日常生活。 但具体什么时候进入人们的日常生活，你别管。 启元机器人相比于其他机器人或者具身智能企业的不同之处在于，网名为「稚晖君」的彭志辉可以为这家公司带来更多的 C 端曝光。彭志辉是智元创新的联合创始人兼 CTO，智元创新在去年收购了 A 股上市公司上纬新材，而上纬启元，即启元机器人则是上纬新材旗下的个人与家庭 C 端消费级机器人赛道的具身智能品牌。 ▲ 智元创新联合创始人兼 CTO 彭志辉 「把机器人卖给普通消费者」一直是一件听起来很有想象力、实际却相当困难的事情。 原因并不复杂。 一台工业机器人只需要在限定环境里，把一件事情稳定重复...
- 作者：刘学文
- 发布时间：2026-09-20 21:10 CST
- 链接：https://www.ifanr.com/1681137?utm_source=rss&utm_medium=rss&utm_campaign=

### 3. iPhone 18 Pro 系列开卖了，但苹果没告诉你的是……
- 摘要：首发购入 iPhone 18 Pro 的朋友，这两天应该已经陆续拿到新机了。 不过，当大家正沉浸在开箱把玩的新鲜感里时，也不妨看一眼这两天数码圈里的「奇妙温差」—— 一边是普通用户忙着撕膜、导数据、挑手机壳；另一边则是各路拆解博主与硬件极客，早就备好了热风枪、显微镜和专业工具，准备把这台新机最底层的秘密一层层剥开。 趁着这股拆机热潮，我们综合了多方的深度拆解与实测发现，带你越过发布会的精美 Keynote，去看看那些真正藏在机身之下的底层秘密。 在不变的机身里，重新设计一切 单看外观，这一代 iPhone 18 Pro 几乎没有给老用户制造任何陌生感，机身尺寸与开孔跟前代一模一样，甚至直接套上...
- 作者：郑廷旭
- 发布时间：2026-09-20 18:24 CST
- 链接：https://www.ifanr.com/1681102?utm_source=rss&utm_medium=rss&utm_campaign=

## InfoQ 中文（infoq-cn，zh，本窗口共 13 条）

### 1. 瞄准 AI 编程、金融等场景，单次成本仅为Opus 5 的1/8！这款国产旗舰模型跻身 AA 榜单全球前三
- 摘要：点击查看原文>
- 作者：李冬梅
- 发布时间：2026-09-20 19:52 CST
- 链接：https://www.infoq.cn/article/9jw1St7ULZijG8XNCWkW?utm_source=rss&utm_medium=article

### 2. 比 Grok、Cursor 都狠？智谱ZCode“偷传代码”风波升级，企业发函追责
- 摘要：点击查看原文>
- 作者：李冬梅
- 发布时间：2026-09-20 19:46 CST
- 链接：https://www.infoq.cn/article/huOiZyyH32MpRwTFkoNe?utm_source=rss&utm_medium=article

### 3. 从“看见文字”到“读懂画面”：AI MediaKit 如何实现视频字幕无痕擦除
- 摘要：点击查看原文>
- 作者：火山引擎视频云
- 发布时间：2026-09-20 19:23 CST
- 链接：https://www.infoq.cn/article/Vqhz90IcQjPlqNXIbfAk?utm_source=rss&utm_medium=article

## IT之家（ithome，zh，本窗口共 81 条）

### 1. 被质疑“偷传代码”后智谱 ZCode 官宣开源：已完成整改并向所有用户道歉
- 摘要：IT之家 9 月 21 日消息，智谱 ZCode 今日宣布，针对社区反馈的 ZCode 产品安全问题， 官方已经完成整改，并向所有用户道歉 。 智谱已将 ZCode 开源 ( https://github.com/zai-org/ZCode )，把代码交给社区监督，让 ZCode 变得开放、透明。 非常感谢此前发现 ZCode 问题的社区开发者，接下来我们将建立常态化的产品安全漏洞机制，欢迎开发者伙伴持续检查和反馈问题，我们会根据问题严重程度给予相应回报。 对于社区中提及的代码数据，我们承诺无留存，也从未将其用于模型训练。完成整改后，我们邀请中国信息通信研究院和绿盟科技开展安全审计，结果如下：...
- 作者：作者： 汪淼
- 发布时间：2026-09-21 09:02 CST
- 链接：https://www.ithome.com/1/005/046.htm

### 2. Rokid 新一代乐奇 AI 眼镜 9 月 24 日数贸会发布
- 摘要：IT之家 9 月 21 日消息，Rokid（乐奇）昨日宣布， 新一代乐奇 AI 眼镜将于 9 月 24 日 14:00 在中国浙江杭州举行的第五届全球数字贸易博览会现场发布 ，口号为 "Less tool. More human"“不是工具，是感官的延伸”。 IT之家了解到，初代乐奇 AI 眼镜基于高通 AR1 SoC，采用 Micro LED + 衍射光波导的双目显示方案，分辨率 480×640、亮度 1500nits、视场角 30°，配备 3024×4032 摄像头，内置 2 扬声器 4 麦克风。
- 作者：作者： 溯波（实习
- 发布时间：2026-09-21 08:48 CST
- 链接：https://www.ithome.com/1/005/042.htm

### 3. 英伟达显卡底层细节揭秘：包含数十个 RISC-V 核心，甚至已接管图形驱动执行
- 摘要：IT之家 9 月 21 日消息，据科技媒体 XDA 报道，英伟达 GPU 实际上包含数十个 RISC-V 核心，部分特殊核心甚至已经接管图形驱动执行。 据报道，这些 RISC-V 核心存在于英伟达 GPU 之中，它们并不负责着色器计算，而是负责图形计算之外的大量额外工作。根据型号不同， 每块 GPU 内部拥有 10-40 个这种核心 。 用户无法对这些核心进行编程。如果核心遭到篡改，GPU 固件甚至无法驱动。其中一个特殊核心甚至已经接管了图形驱动程序的大量工作，这种情况从 2018 年开始就已经存在。 据悉，英伟达在使用 RISC-V 核心之前使用的是 Falcon（IT之家注：快速逻辑控制器...
- 作者：作者： 潞源
- 发布时间：2026-09-21 08:41 CST
- 链接：https://www.ithome.com/1/005/039.htm

## 雷峰网（leiphone，zh，本窗口共 8 条）

### 1. 别把杰作留在实验室，张江见 2026 GDPS 国际具身智能技能大赛·高校赛队招募
- 摘要：具身智能正在从「展示品」变成「生产力」。而这一年，国家把真题摆上了桌面，工信部联合国务院国资委启动《2026年度人形机器人与具身智能实景实训专项行动》，九大重点场景面向全球求解： 生产制造、检测分析、维修维护、仓储物流、配送零售、医疗康养、安全生产、应急救援、防灾减灾 。 上海作为先行城市承接国家任务。 10月23—25日，上海·张江科学会堂 ， 2026 全球开发者先锋大会（GDPS）暨国际具身智能技能大赛，一场面向高校赛队的实景大考正式开启。这不是一场普通比赛， 参赛即路演，获奖即融资 。 炼过赛场的，才是真未来生产力。 谁可以来 面向 国内外高校与科研机构 的学生科研团队。 每队不超过5...
- 发布时间：2026-09-20 16:08 CST
- 链接：https://www.leiphone.com/category/industrynews/QmCxO9BKrABdNFbB.html

### 2. 剪映发布全新AI能力，推进多端智能提效，支持一站式创作
- 摘要：9月20日，剪映举办“AI新创作发布会”，围绕不同创作需求推出剪映Hub、AI创作助手“小映”等多个AI新功能，并升级创作者生态。 从专业创作工作台到移动端AI助手，再到模板与创作者服务升级，剪映此次发布的多项能力都指向同一个目标：让AI更多承担生成、整理和重复操作，同时保留创作者对内容、表达和风格的最终判断。随着创作工具、工作流与创作者生态进一步衔接，不同经验阶段的用户都可以从自己的想法和素材出发，更顺畅地完成作品。 剪映针对不同创作需求，打造全场景智能创作平台 剪映专业版：智能提效与专业能力并进，支持一站式创作 面对专业创作者频繁切换工具、重复操作耗时等问题，剪映专业版推出一站式创作工作台...
- 发布时间：2026-09-20 15:07 CST
- 链接：https://www.leiphone.com/category/industrynews/57VaKsFFtr52ic0r.html

### 3. 沙利文发布2026年智能体市场研究报告：WorkBuddy稳居企业级、个人应用双榜第一
- 摘要：9月20日，全球权威机构沙利文发布《2026年全球桌面AI智能体市场研究报告》，腾讯WorkBuddy同时位列中国个人端桌面智能体榜单与企业级桌面智能体榜单第一，继续保持双端领先地位。 报告以“产品技术领先”和“用户落地实效”两项综合指标衡量桌面AI智能体竞争力。 “产品技术领先指数”聚焦技术创新，重点评估：Agentic能力、Harness 工程、模型适配与可用性、扩展与开放能力，覆盖任务规划、工具调用、多 Agent 协作、记忆管理、Computer Use、权限控制、错误恢复、MCP/Skills 体系与第三方集成等关键指标。 “用户落地实效指数”则重点关注：桌面端用户体验、多端互联生态...
- 发布时间：2026-09-20 12:14 CST
- 链接：https://www.leiphone.com/category/industrynews/U0o8Z4sG9l26lvTQ.html

## 开源中国（oschina，zh，本窗口共 10 条）

### 1. openKylin 成立 ZephyrProject SIG：加速 Zephyr 国内生态落地与技术创新
- 摘要：近年来，实时操作系统（RTOS）正从单一内核向平台化、生态化演进，应用场景也从单 MCU 控制走向异构计算与云边协同，开源生态的重要性日益凸显。但在国内，Zephyr 的基础设施与配套支持仍不够完善。为此，麒麟软件牵头在 OpenAtom openKylin（以下简称“openKylin”）社区成立了 ZephyrProject SIG，面向工控、具身智能、...
- 发布时间：2026-09-20 21:34 CST
- 链接：https://www.oschina.net/news/502623

### 2. MiniMax Code CLI 开源，取得了 76.7% 的任务通过率
- 摘要：MiniMax 把 AI 编程工具的核心组件开源了。MiniMax Code CLI 的 v0.4.12 版本面向全球开发者正式开放，并用 MIT 协议放出了源码——它是 MiniMax Code 客户端的核心组件，装上就能直接用命令行生成、调试代码。 性能数据来自 FrontierHarness Eval 评测：76.7% 的任务通过率，成功任务耗时中位数为 4 分 33 秒，两项指标...
- 发布时间：2026-09-20 19:04 CST
- 链接：https://www.oschina.net/news/502619/minimax-code-cli

### 3. 百度搭子用户规模环比增长9倍，发布企业版移动端、开发平台与共创计划
- 摘要：9月20日，百度智能云超级智能体大会深圳站举行。会上，百度搭子升级企业版多人协作能力，发布企业版移动端和智能体开发平台，并启动生态共创计划。数据显示，百度搭子用户规模环比增长9倍，交付物需求环比增长4.3倍，专家套件使用量环比增长7.3倍。 百度集团执行副总裁、百度智能云事业群总裁沈抖表示，企业智能化需要通...
- 发布时间：2026-09-20 16:41 CST
- 链接：https://www.oschina.net/news/502615

## 量子位（qbitai，zh，本窗口共 7 条）

### 1. 刚刚，剪映发了个大的：AI生视频和AI剪辑的壁，被打破了！
- 摘要：剪映Hub+剪映助手，好用
- 作者：十三
- 发布时间：2026-09-20 22:30 CST
- 链接：https://www.qbitai.com/2026/09/492973.html

### 2. 华为首发企业AI白皮书：AI让员工更快了，怎样让整个企业受益？
- 摘要：AI越来越能干，企业该怎么用
- 作者：henry
- 发布时间：2026-09-20 22:23 CST
- 链接：https://www.qbitai.com/2026/09/493068.html

### 3. 一张3090就能跑！全栈国产模型，把AI办公搬到企业本地
- 摘要：AI办公这块蛋糕，中国电信可能要先切走一块了。
- 作者：henry
- 发布时间：2026-09-20 20:22 CST
- 链接：https://www.qbitai.com/2026/09/492946.html

## 少数派（sspai，zh，本窗口共 1 条）

### 1. 派早报：微软高管称 AI 爬取是人类历史上最大的劳动成果盗窃
- 摘要：微软高管称 AI 爬取是人类历史上最大的劳动成果盗窃 12306 称第三方购票可能更慢或失败 特朗普提议为人工智能改名 谷歌在 Android 17 中加入 Pixel 独占的 API iPhone 18 Pro Max 支持固件限制电量以便发运 苹果硬件工程副总裁表示不建议贴膜 看看就行的简讯 少数派的近期动态 你可能错过的好文章 查看全文
- 作者：少数派编辑部
- 发布时间：2026-09-21 06:26 CST
- 链接：https://sspai.com/post/114788

## 钛媒体（tmtpost，zh，本窗口共 24 条）

### 1. 边缘算力升级，工控机站上AI风口
- 摘要：文 | 半导体产业纵横 今年，涨价已经成为电子行业的主旋律，工业自动化产品也在这一轮成本压力中重新定价。 各大工业巨头早已陆续发布涨价函，施耐德Acti9/Acti9-S系列微型断路器全系涨价约6%；同期ATS22系列软起动器、STB Advantys全系列l/O及Momentum系列控制器、以太网网关模块、以太网通讯模块、工控机等产品也在涨价。 欧姆龙发布价格调整通知，包括PLC、HMI、机器人、继电器、传感器、开关、温控器等工业自动化产品涨价，涨价幅度最小为5%，并联机器人部分产品涨价幅度甚至高达50%。 在制造业振兴政策的持续引导、新能源，芯片制造等战略行业需求释放、以及具身机器人等新兴...
- 作者：半导体产业纵横
- 发布时间：2026-09-21 08:50 CST
- 链接：https://www.tmtpost.com/8146457.html

### 2. 马斯克要把“帝国”装进特斯拉？不想只卖车了
- 摘要：文 | 不慌实验室，作者 | 任天勤，编辑 | 陈肖冉 马斯克正试图将制造、能源、AI、通信与金融入口深度打通，把特斯拉从单一车企升级为全域商业生态载体。SpaceX、中国供应链、重卡充电与X平台交易，看似分散，背后却是同一条清晰主线。 四线并进 近日，马斯克被问及特斯拉与SpaceX是否会进一步整合时，以“好问题”暧昧回应，并再度强调双方在芯片、卫星通信、智能制造体系的深度协同。 不过，目前仅为口头表态，暂无正式合并方案、董事会决议及监管文件落地。可将其视作马斯克对市场的提前试探，但若直接判定两家公司即将合并，仍为时过早。 国内产业链传出新消息，特斯拉已启动新一轮中国供应链审厂工作，核心审核...
- 作者：不慌实验室
- 发布时间：2026-09-21 08:46 CST
- 链接：https://www.tmtpost.com/8146444.html

### 3. 李想的投资野心：当欣旺达二股东，“扫货”机器人公司
- 摘要：文 | 多空象限，作者｜刘日斤 李想又出手搞投资了！ 2026年9月，欣旺达最新一轮C++轮融资细节的披露，理想汽车拟出资26.5亿元增资欣旺达动力，认购8.79%的股份。 交易完成后，理想汽车相关主体将间接持有11.17%的股份，跃升为欣旺达动力的第二大股东，推动这只动力电池独角兽的估值冲破300亿元大关。 这已经不是李想第一次押注欣旺达。 早在2022年，理想就曾投入4亿元成为欣旺达汽车电池的股东；2025年，双方又以50:50的股比成立了电池合资公司。到2026年，理想再拿出26.5亿元，把自己从一个电池客户，变成供应商的重要股东。 与此同时，理想的资本触角正在从电池伸向自动驾驶，再伸向...
- 作者：多空象限
- 发布时间：2026-09-21 08:42 CST
- 链接：https://www.tmtpost.com/8146396.html

## 智东西（zhidx，zh，本窗口共 4 条）

### 1. 又一国产MoE旗舰模型登场！跻身全球开源第三，价格对标DeepSeek-V4-Pro
- 摘要：智东西 作者 | 程茜 编辑 | 李水青 智东西9月20日报道，今日，阶跃星辰发布新一代MoE旗舰模型 Step 5 Preview 。该模型专为真实世界Agentic任务打造，总参数量600B、激活参数27B，支持100万Token上下文窗口，原生支持文本与视觉输入。 在全球AI榜单Artificial Analysis Intelligence Index中，Step 5 Preview得分 44分 ，位居 开源模型第三 ，排在其前面的开源模型是Qwen3.8 Max（0902）、GLM-5.3（max）。 根据阶跃公开的基准测试结果，Step 5 Preview在Agent长周期CLI任...
- 作者：程茜
- 发布时间：2026-09-20 18:45 CST
- 链接：https://zhidx.com/p/595573.html

### 2. 10岁小孩姐，都能轻松给机器人编程！稚晖君连发两款万元级机器人
- 摘要：机器人前瞻（公众号：robot_pro） 作者 | 许丽思 编辑 | 漠影 机器人前瞻9月20日报道，今天下午，启元机器人在上海一口气发布了两款面向家庭场景的个人机器人——Q1和T1。 两款产品已经正式开放购买，将于10月1日起按订单顺序陆续发货。价格方面，Q1标准版售价 19999元； 探索版Q1拥有开放SDK&HDK、硬件拓展接口，支持全栈二次开发、支持技能应用开发，为 26999元。 T1标准版售价 19999元 ；Pro版T1具备0rin高算力芯片、360°全向感知智能避障、低电量自动导航回充、跟随载物开放二次开发接口等功能，价格为 29999元。 走进启元新品发布会现场，这两款机器人...
- 作者：许 丽思
- 发布时间：2026-09-20 17:58 CST
- 链接：https://zhidx.com/p/595607.html

### 3. 刚刚，中国最大独立Token工厂又融资，年内已融29亿
- 摘要：智东西 作者 | 王涵 编辑 | 冰倩 智东西9月20日报道，今天，AI基础设施企业 硅基流动（SiliconFlow） 宣布已先后完成 B+轮二期和C轮融资 ，投资方包括中国互联网投资基金、国新基金、中国移动链长基金等。至此，该公司 2026年度累计融资金额近29亿元 。 据硅基流动披露，其本次披露的两轮融资将重点用于加大推理引擎、异构算力调度、模型与芯片适配等核心技术研发投入，强化Token供应平台能力建设，并加快全球市场拓展。 自2024年3月以来，硅基流动已完成 8轮上市前融资 。今年6月，硅基流动宣布已完成 超20亿元B轮融资 。（ 超20亿！智谱投的AI云厂商融资了，跟阿里火山百度...
- 作者：王 涵
- 发布时间：2026-09-20 15:20 CST
- 链接：https://zhidx.com/p/595555.html

# Tier 3 — 社交 / 聚合

## GitHub Trending (daily)（github-trending，en，本窗口共 8 条）

### 1. Open-Dev-Society/OpenStock
- 摘要：OpenStock is an open-source alternative to expensive market platforms. Track real-time prices, set personalized alerts, and explore detailed company insights — built openly, for everyone, forever free. https://openstock-ods.vercel.app New from Open Dev Society: kitbash . Before you build, find out w...
- 发布时间：2026-09-20 17:54 CST
- 链接：https://github.com/Open-Dev-Society/OpenStock

### 2. higgsfield-ai/higgsfield
- 摘要：Fault-tolerant, highly scalable GPU orchestration, and a machine learning framework designed for training models with billions to trillions of parameters higgsfield - multi node training without crying Higgsfield is an open-source, fault-tolerant, highly scalable GPU orchestration, and a machine lea...
- 发布时间：2026-09-20 17:54 CST
- 链接：https://github.com/higgsfield-ai/higgsfield

### 3. docling-project/docling
- 摘要：Get your documents ready for gen AI https://docling-project.github.io/docling Docling What is Docling ? Docling simplifies document processing by parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the generative AI ecosystem. Features 🗂️ Parsing...
- 发布时间：2026-09-20 17:54 CST
- 链接：https://github.com/docling-project/docling

## Hacker News (AI stories)（hackernews-ai，en，本窗口共 133 条）

### 1. ZCode: silently uploading your Git history to the cloud
- 作者：fourfire
- 发布时间：2026-09-21 08:01 CST
- 链接：https://news.routley.io/posts/inside-zcode-silently-uploading-your-git-history-to-the-cloud.html

### 2. Amiga Unix, Again
- 摘要：Year of the Amiga Unix Desktop 2026 Amiga Unix, again Amiga Unix — Amix — was Commodore's System V Release 4 for the Amiga: shipped in 1990–92 for the A2500UX and A3000UX, then left where it stood. amigaux.org is an unofficial community project that picks it up again: Amix on 68040 and 68060 machine...
- 作者：doener
- 发布时间：2026-09-21 07:57 CST
- 链接：https://amigaux.org/

### 3. DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR
- 摘要：An Open-source RL System from ByteDance Seed and Tsinghua AIR - BytedTsinghua-SIA/DAPO
- 作者：the_arun
- 发布时间：2026-09-21 07:19 CST
- 链接：https://github.com/BytedTsinghua-SIA/DAPO

## Product Hunt — AI（producthunt-ai，en，本窗口共 3 条）

### 1. Epismo OS
- 摘要：Keep your work when you switch AI tools Discussion | Link
- 作者：Hiroki
- 发布时间：2026-09-20 04:05 CST
- 链接：https://www.producthunt.com/products/epismo

### 2. Answers by Context.dev
- 摘要：Give it a research task + the JSON shape you want back. Discussion | Link
- 作者：Ely
- 发布时间：2026-09-19 16:54 CST
- 链接：https://www.producthunt.com/products/context-dev

### 3. Minicart
- 摘要：Launch your store. Let AI run the busywork. Discussion | Link
- 作者：Ben Lang
- 发布时间：2026-09-15 01:22 CST
- 链接：https://www.producthunt.com/products/minicart

## Reddit AI subreddits (new)（reddit-ai-new，en，本窗口共 393 条）

### 1. How to make Claude 3D Model accurately?
- 摘要：I’ve been using the Claude desktop app in Claude code mode with the goal to recreate this character. Sadly Claude’s attempts to recreate it off of pictures and descriptions has been awful. However when I told Claude to create a diorama of Tokyo it actually looked really good. Does anyone know how to...
- 作者：Secure_Value_6005
- 发布时间：2026-09-21 09:15 CST
- 链接：https://www.reddit.com/gallery/1wlyprh

### 2. H3 minimax output feel different after a comfyui update
- 摘要：So..the last few 2 days, i went to update my comfyui portable and suddenly my work flow went OOM, so i enquire with Chatgpt which seems that Sage attention and my pytorch was causing issue but i was not using Sage attention as it was on disable and i was using comfyui kitchen attention, so i uninsta...
- 作者：Leonviz
- 发布时间：2026-09-21 09:13 CST
- 链接：https://www.reddit.com/r/StableDiffusion/comments/1wlyo33/h3_minimax_output_feel_different_after_a_comfyui/

### 3. Codex Computer use not working on Sol?
- 摘要：Astra has been working fine to use computer use for my use case but literally only works for 10 minutes or less before the 5hr limit is reached on plus plan even on light. So I tried Luna Light and it wouldn’t work. Neither would Sol light citing an issue finding the “app” (it just needs to use desk...
- 作者：FamilyNP
- 发布时间：2026-09-21 09:12 CST
- 链接：https://www.reddit.com/r/OpenAI/comments/1wlynhe/codex_computer_use_not_working_on_sol/

## 智源社区（baai-hub，zh，本窗口共 18 条）

### 1. Gemini 4 Pro首测夯爆了！谷歌偷偷杀回第一
- 摘要：新智元报道 谷歌真要彻底翻身了！ 这几天，一个披着「gemini-3.8-flash」马甲的神秘模型，在大模型竞技场Arena上现身。 在多轮盲测中，AI圈瞬间沸腾：这绝对是谷歌「隐藏款」Gemini 4 Pro。 随之，一大批震撼Demo瞬间涌出。 就在今天，Gemini 4 Pro生成的一只机械蝴蝶刷屏全网，仅用十分钟大功告成，而Fable足足耗费了约30分钟。 发光的机械羽翼、精密咬合的发条齿轮、流畅灵动的动态表现—— Gemini 4 Pro和Fable 5.1两者都展现出了极高的水准，但速度差距，已经说明了一切。 现在，所有人全都在盯着「OA两巨头」，谁能想到，谷歌已经在背后偷偷发力...
- 作者：新智元
- 发布时间：2026-09-21 09:00 CST
- 链接：https://hub.baai.ac.cn/view/58132

### 2. 谷歌还有大招！最新模型Mathematica泄露
- 摘要：新智元报道 大模型做数学题做到「颅内高潮」，你见过吗？ 在大多数人的印象里，AI做数学题四平八稳、逻辑缜密。 哪怕是当前最顶尖的推理模型，思维链无非也是一段段机械自语 ： 第一步，设 x 为未知数；第二步，将两边同时平方；第三步，根据引理得出矛盾…… 但今天这个谷歌大模型，彻底颠覆了人类对AI的认知。 近日，知名科技博主与爆料人 lyra 在社交平台上晒出了数张谷歌内部评测模型的卡片截图。 截图中，一款代号为 Mathematica （基于尚未正式发布的 DeepThink V3）的数学特化变体赫然在列。 更让整个科技界瞠目结舌的是它的「原始思维链」—— 在推导一道复杂的丢番图方程（Dioph...
- 作者：新智元
- 发布时间：2026-09-21 08:50 CST
- 链接：https://hub.baai.ac.cn/view/58131

### 3. 广州站—Schrödinger计算化学驱动的药物发现全流程实战研修班
- 摘要：前言 Schrödinger 套件 是行业广泛使用的 集成化计算药物设计平台 ，其独特优势在于 深度融合了基于物理的精确算法（如FEP+自由能微扰、Desmond分子动力学、Glide对接）与数据驱动的机器学习模型 ，同时覆盖从靶点结构预测（同源建模、口袋检测）到虚拟筛选（对接、药效团、形状匹配），再到先导优化（Ligand Designer、骨架跃迁）和最终候选物评价（MM-GBSA、ADME预测）的完整链条。这一集成化工作流不仅大幅减少不同软件之间的数据转换误差，更能提供与实验高度吻合的预测精度，已被众多制药企业广泛采用。 本课程 拒绝照本宣科 ，由具有多年工业级项目经验的讲师团队亲自设计...
- 作者：DrugAI
- 发布时间：2026-09-21 00:40 CST
- 链接：https://hub.baai.ac.cn/view/58130

---
共列出 91 条（窗口内采集总数 896 条，来自 33 个信源）

## OpenClaw 推送提示
请基于本文件生成中文 Daily AI News 推送，不要联网，不要抓原文，不要扩展搜索。
优先 Tier 1 一手来源和国内外媒体中被多个信源同时报道的事件；Tier 3 社交条目只做补充。
每日只保留最新内容，覆盖更新。
