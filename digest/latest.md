# Daily AI News（原文采集，国内外）
生成时间：2026-09-25 03:22 CST
时间窗口：最近 24 小时内采集到的条目；每个信源最多列 3 条，按发布时间倒序。

> 本文件由 ai-news-collector 自动生成（github.com/xbbwa/ai-news-collector，data 分支），每小时覆盖更新。
> OpenClaw 推送时只应读取本文件，不要联网、不抓全文、不扩展搜索。
> 摘要为原文节选（未翻译、未清洗）；英文条目请在推送时翻译成中文。

# Tier 1 — 一手来源（实验室 / 公司 / 论文）

## Anthropic News（anthropic-news，en，本窗口共 1 条）

### 1. Claude discovers a novel enzyme system with CRISPR-like repeats
- 摘要：We’re introducing a new life sciences research group and laboratory at Anthropic. Our focus is on fundamental biology research using Claude: exploring datasets of DNA to identify uncharacterized protein families, generating hypotheses at scale, and testing them through experiments in the lab. This p...
- 发布时间：2026-09-23 00:00 CST
- 链接：https://www.anthropic.com/news/claude-discovers-novel-enzyme-system

## Apple Machine Learning Research（apple-ml，en，本窗口共 3 条）

### 1. Compressing Streaming Neural Audio Encoders via Latent-Space Distillation
- 摘要：System-wide Dictation on Apple devices runs entirely on-device, and the speech it transcribes reaches the foundation model through a tokenizer: an encoder that maps short windows of waveform onto the representation the language model reads. Because that model is sparsely activated under Instruction-...
- 发布时间：2026-09-24 08:00 CST
- 链接：https://machinelearning.apple.com/research/latent-space-distillation

### 2. A Practical Recipe for Semi-Supervised Federated ASR: Online Pseudo-Labels with Server Update Stabilization
- 摘要：Semi-supervised federated learning (SSFL) trains models on clients’ unlabeled data using a teacher to generate pseudo-labels, with a small labeled seed dataset on the server. Automatic Speech Recognition (ASR) is particularly fragile here: pseudo-label errors compound across the output sequence and...
- 发布时间：2026-09-24 08:00 CST
- 链接：https://machinelearning.apple.com/research/practical-recipe-federated-asr

### 3. How to Guide Your Language Flow
- 摘要：We introduce a new method to guide flow matching models. Our approach, which we call probe guidance, uses the frozen internal states of an existing diffusion model to construct a guidance signal. This works using a similar principle as autoguidance, but eliminates the need for an additional forward...
- 发布时间：2026-09-23 08:00 CST
- 链接：https://machinelearning.apple.com/research/guide-language-flow

## arXiv cs.AI（arxiv-cs-ai，en，本窗口共 4 条）

### 1. MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games
- 摘要：arXiv:2609.06563v2 Announce Type: replace Abstract: Social deduction games (SDGs) require agents to reason under partial observability by maintaining relational beliefs about hidden roles and team alignments. While recent LLM-agent approaches improve gameplay through prompting and preference optimiz...
- 作者：Yechan Hwang, Sangjun Bae, Jeongmo Kim, Sangwoo Bang, Seungyul Han
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.06563

### 2. What Does Multi-Agent LLM Debate Actually Change? A Layered Analysis of Disagreement and Answer Quality
- 摘要：arXiv:2609.08016v2 Announce Type: replace Abstract: Multi-agent debate, in which several LLMs exchange arguments before producing an answer, is widely assumed to improve answer quality by surfacing genuine disagreement. That disagreement is hard to verify, and no single signal can settle it, so we o...
- 作者：Chen Qian
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.08016

### 3. Parameter-Free Dynamic Regret under Heavy-Tailed Noise
- 摘要：arXiv:2607.27073v3 Announce Type: replace-cross Abstract: We study online convex optimization with one unbiased stochastic subgradient per round and noise having a finite $p$-th central moment, where $p\in(1,2]$ is unknown. For a bounded convex domain of diameter $D$, subgradients bounded by $G$, no...
- 作者：Vaneet Aggarwal
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2607.27073

## arXiv cs.CL（arxiv-cs-cl，en，本窗口共 108 条）

### 1. COMED: The Missing Middle Between Routing and Collaboration in Multi-LLM Inference
- 摘要：arXiv:2609.26913v1 Announce Type: new Abstract: No single Large Language Model (LLM) is uniformly reliable across queries, motivating multi-model inference systems that either route among models or combine their outputs. However, routing stops after selecting an initial model, while dense collaborat...
- 作者：Norah Alballa, Wenxuan Zhang, Salma Kharrat, Fares Fourati, Zafar Ayyub Qazi, Mo...
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26913

### 2. Recognized but Not Produced: A Generation Benchmark for Culturally Specific Kinship Terms
- 摘要：arXiv:2609.26942v1 Announce Type: new Abstract: Current literature evaluates large language models (LLMs) on multilingual kinship understanding using multiple choice benchmarks, treating it as a recognition problem. We instead prompt five open weight LLMs to generate kinship terms in three non Weste...
- 作者：Sahil Pardasani, Madhusudan Singh
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26942

### 3. Classifying Interpretive Canons at the Sentence Level: A Benchmark from the German Federal Constitutional Court
- 摘要：arXiv:2609.26945v1 Announce Type: new Abstract: Judicial reasoning remains challenging for large language models (LLMs) to analyze. This paper contributes a sentence-level benchmark for evaluating the ability of LLMs to classify interpretive canons as articulated by Larenz in the tradition of Savign...
- 作者：Felix Ringe
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26945

## arXiv cs.CV（arxiv-cs-cv，en，本窗口共 163 条）

### 1. AgroBench: A Reproducible Multimodal Benchmark for Weakly Supervised Crop Yield Learning from County Statistics and Pixel Observations
- 摘要：arXiv:2609.26809v1 Announce Type: new Abstract: Reliable agricultural yield statistics are typically reported at coarse administrative scales, whereas modern geospatial machine learning methods require spatially explicit, pixel level supervision. This mismatch has limited the development of large-sc...
- 作者：Udaiveer Singh, Rajiv Ranjan, Shashank Tamaskar, Dharmendra Saraswat
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26809

### 2. Cross-Modal Contrastive Learning from Histopathology and CT for Automated Renal Cell Carcinoma Grading
- 摘要：arXiv:2609.26920v1 Announce Type: new Abstract: Background: Clear cell renal cell carcinoma (ccRCC) exhibits substantial clinical heterogeneity, and accurate grade assessment is essential for risk stratification and treatment planning. However, conventional grading requires invasive tissue sampling....
- 作者：Amit Das, Tanmay Shukla, Naofumi Tomita, Faraz Farhadi, Jessica Sin, Ari Hakimi,...
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26920

### 3. A 3D Pose-Based Ensemble Framework for Cricket Shot Classification and Automated Biomechanical Analysis
- 摘要：arXiv:2609.26923v1 Announce Type: new Abstract: Cricket is one of the most celebrated sports world-wide, and technological advancement has become deeply embedded in how the modern game is analyzed and coached. Cricket shot classification and automated performance analysis add a further dimension to...
- 作者：Sourav Shome, M. D. Ashiquzzaman Rahad, Rameswar Debnath
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26923

## arXiv cs.LG（arxiv-cs-lg，en，本窗口共 254 条）

### 1. The Drift Contract: Spectral Updates for Depth-Robust Local Learning
- 摘要：arXiv:2609.26811v1 Announce Type: new Abstract: Local learning trains each layer with its own auxiliary loss and no global backward pass, which makes layer updates structurally parallel. Two problems have kept it marginal: accuracy degrades as depth grows, and hyperparameters are fragile. We apply M...
- 作者：Fabien Polly
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26811

### 2. Signal2Symbol: Neuro-Symbolic Temporal Reasoning for Explainable Physiological Time-Series Anomaly Detection
- 摘要：arXiv:2609.26820v1 Announce Type: new Abstract: Physiological time series such as electrocardiograms (ECG) and electroencephalograms (EEG) exhibit complex temporal structure, substantial acquisition variability, and a strong need for transparent decision-making. Although deep models can achieve high...
- 作者：Naser Mansour, Sidahmed Benabderrahmane, Ameer Rahwan
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26820

### 3. HARN: Hierarchical Associative Resonance Network for Event-Driven Multi-Timeframe Forecasting
- 摘要：arXiv:2609.26822v1 Announce Type: new Abstract: Financial time series evolve across multiple temporal resolutions, challenging forecasting systems to incorporate newly available information without repeatedly recomputing unchanged representations. We introduce HARN, a Hierarchical Associative Resona...
- 作者：Nabeel Ahmad Saidd
- 发布时间：2026-09-24 12:00 CST
- 链接：https://arxiv.org/abs/2609.26822

## AWS Machine Learning Blog（aws-ml-blog，en，本窗口共 6 条）

### 1. Speaker-labeled transcription with WhisperX on SageMaker AI
- 摘要：Any team working with spoken audio hits the same wall with generic speech-to-text. Think contact-center calls, all-hands meetings, podcasts, depositions, and broadcast media. These workloads need two things that standard transcription gets wrong. First, timestamps land at the utterance level, off by...
- 作者：Ayush Sharma
- 发布时间：2026-09-25 00:20 CST
- 链接：https://aws.amazon.com/blogs/machine-learning/speaker-labeled-transcription-with-whisperx-on-sagemaker-ai/

### 2. Build a multi-account AI agent with AgentCore Gateway and MCP
- 摘要：Enterprises increasingly want AI agents that can reason over data spread across many AWS accounts without copying or centralizing it. Each team keeps its data in its own account for good reasons: clear ownership, scope isolation, and independent deployment lifecycles. But an agent that sees only one...
- 作者：Senthil Kamala Rathinam
- 发布时间：2026-09-25 00:12 CST
- 链接：https://aws.amazon.com/blogs/machine-learning/build-a-multi-account-ai-agent-with-agentcore-gateway-and-mcp/

### 3. Aderant builds intelligent ticket triage with Amazon Nova
- 摘要：This guest post is co-written by Angela Mapes and Adam Walker of Aderant. In this post, we share how Aderant , a global provider of business management software for the legal industry, built an intelligent ticket triage system using Amazon Nova Lite through Amazon Bedrock. Aderant’s solution automat...
- 作者：Angela Mapes
- 发布时间：2026-09-25 00:06 CST
- 链接：https://aws.amazon.com/blogs/machine-learning/aderant-builds-intelligent-ticket-triage-with-amazon-nova/

## Databricks Blog（databricks-blog，en，本窗口共 2 条）

### 1. Deploy and manage coding agents at scale with the Unity Gateway CLI
- 摘要：In the last six months, GPT-6, Claude Opus 5.5, Gemini 3.8, and Grok 4.7 all shipped,...
- 作者：The Databricks AI Product; Engineering Team
- 发布时间：2026-09-25 00:46 CST
- 链接：https://www.databricks.com/blog/deploy-and-manage-coding-agents-scale-unity-gateway-cli

### 2. How I built agent-based security reviews on Databricks
- 摘要：We already had automation in parts of our security review process. It was useful,...
- 作者：Angel De Leon
- 发布时间：2026-09-24 10:00 CST
- 链接：https://www.databricks.com/blog/how-i-built-agent-based-security-reviews-databricks

## Google DeepMind Blog（deepmind-blog，en，本窗口共 1 条）

### 1. Introducing Gemini 3.8 Live with Live Avatar
- 摘要：Introducing Gemini 3.8 Live with Live Avatar, which brings near real-time visual presence to Gemini’s conversational AI.
- 作者：Shuo-yiin Chang; CJ Zheng
- 发布时间：2026-09-25 00:20 CST
- 链接：https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/

## GitHub Blog（github-blog，en，本窗口共 2 条）

### 1. AI-powered fuzzing with the GitHub Security Lab Taskflow Agent
- 摘要：If you’re new to fuzzing and want to learn the fundamentals first, check out our Fuzzing 101 course at gh.io/fuzzing101 . Continuous fuzzing is not a magic solution that solves all your problems . Even projects that have been enrolled in OSS-Fuzz for years can still hide critical bugs, and the reaso...
- 作者：Antonio Morales
- 发布时间：2026-09-25 02:26 CST
- 链接：https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/

### 2. Rendering huge pull requests in the GitHub Copilot app
- 摘要：Broad refactors and migrations often have to land as one change. Stacked pull requests are a great way to split work into smaller changes, which makes reviews easier and helps teams ship with less risk. But some changes, like this one, can’t be split cleanly. That leaves you with a single pull reque...
- 作者：Alberto Gimeno
- 发布时间：2026-09-24 02:29 CST
- 链接：https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/

## Google — The Keyword (AI)（google-ai-blog，en，本窗口共 1 条）

### 1. Google Beam expands with new regions, partners, and customers
- 摘要：We’re expanding Google Beam to five new countries, and partnering with Industrious for an extended network.
- 作者：Aaron Luber
- 发布时间：2026-09-24 02:00 CST
- 链接：https://blog.google/innovation-and-ai/technology/research/google-beam-expansion/

## Google Cloud Blog — AI & ML（google-cloud-ai，en，本窗口共 3 条）

### 1. Power your agents: Gemini 3.8 Live with Live Avatar is now generally available
- 摘要：Following our announcement of Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking last week, we are thrilled to share that Gemini 3.8 Live with Live Avatar is now generally available in Gemini Enterprise . First previewed at Google Cloud Next 2026 , the technology is now officially ready for enter...
- 作者：Fabien Blanc-paques
- 发布时间：2026-09-24 23:00 CST
- 链接：https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-8-live-with-live-avatar-is-now-generally-available/

### 2. How growing Latin American midsize businesses are building in the AI era
- 摘要：Latin America’s small and medium-sized businesses are the heartbeat of the region's economy — accounting for more than 60% of total employment in the region, according to United Nations estimates. And just like their enterprise peers, everywhere you look, ambitious teams are moving fast to embrace A...
- 作者：Andre Alves
- 发布时间：2026-09-24 22:30 CST
- 链接：https://cloud.google.com/blog/topics/customers/how-midsize-latam-companies-build-with-ai/

### 3. The three things today's hottest startups are looking for in their AI stack
- 摘要：Google Cloud has become the platform of choice for startups building AI. Our uniquely complete stack — including a choice of first- and third-party compute and models ; our platform for building and managing agents; and our products for securing AI workloads — has emerged as the single most importan...
- 作者：Darren Mowry
- 发布时间：2026-09-24 21:00 CST
- 链接：https://cloud.google.com/blog/topics/startups/the-three-things-todays-hottest-startups-are-looking-for-in-their-ai-stack/

## Hugging Face Daily Papers（hf-daily-papers，en，本窗口共 9 条）

### 1. WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents
- 摘要：AI research agents need reliable knowledge of how their experiments change outcomes. We introduce WhatWorkedBench to measure experimental understanding, the accuracy of predictions about component changes after budgeted experimentation. Agents inspect code, select measurements, and submit a response...
- 作者：Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li
- 发布时间：2026-09-23 04:00 CST
- 链接：https://arxiv.org/abs/2609.27490

### 2. Hunyuan-A13B Technical Report
- 摘要：We present Hunyuan-A13B, an open-source large language model based on a Mixture-of-Experts architecture. It contains 80 billion total parameters but activates only 13 billion during inference, balancing model capability, computational efficiency, and deployment cost. The model is pretrained on a rig...
- 作者：Tencent Hunyuan Team, Ao Liu, Botong Zhou, Can Xu, Chayse Zhou, ChenChen Zhang,...
- 发布时间：2026-09-23 04:00 CST
- 链接：https://arxiv.org/abs/2609.27284

### 3. Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents
- 摘要：Agentic memory systems reuse past experience to improve future performance, yet most existing designs curate memory at write time: once a task is completed, its trajectory is distilled into a fixed artifact, such as a reflection, workflow, skill, or reasoning strategy, that is later retrieved by sim...
- 作者：Yefan Zhou, Yang Li, Zeyu Leo Liu, Semih Yavuz, Shafiq Joty
- 发布时间：2026-09-23 04:00 CST
- 链接：https://arxiv.org/abs/2609.27334

## Hugging Face — model releases (Chinese labs)（hf-models-cn，en，本窗口共 22 条）

### 1. internlm/InternLumina-U2
- 摘要：transformers, safetensors, diffusion, multimodal, unified-model, image-generation, image-editing, vision-language, en, license:apache-2.0, endpoints_compatible, region:us
- 作者：internlm
- 发布时间：2026-09-24 20:53 CST
- 链接：https://huggingface.co/internlm/InternLumina-U2

### 2. inclusionAI/Ling-mini-2.0
- 摘要：text-generation, transformers, safetensors, bailing_moe, conversational, custom_code, arxiv:2507.17702, base_model:inclusionAI/Ling-mini-base-2.0, base_model:finetune:inclusionAI/Ling-mini-base-2.0, license:mit, region:us
- 作者：inclusionAI
- 发布时间：2026-09-24 18:57 CST
- 链接：https://huggingface.co/inclusionAI/Ling-mini-2.0

### 3. inclusionAI/Ling-flash-2.0
- 摘要：text-generation, transformers, safetensors, bailing_moe, conversational, custom_code, arxiv:2507.17702, base_model:inclusionAI/Ling-flash-base-2.0, base_model:finetune:inclusionAI/Ling-flash-base-2.0, license:mit, region:us
- 作者：inclusionAI
- 发布时间：2026-09-24 18:55 CST
- 链接：https://huggingface.co/inclusionAI/Ling-flash-2.0

## Hugging Face — model releases (international labs)（hf-models-intl，en，本窗口共 7 条）

### 1. LiquidAI/LFM2.5-VL-3B-DSpark-GGUF
- 摘要：image-text-to-text, llama.cpp, gguf, speculative-decoding, dspark, lfm2, lfm2-vl, draft-model, base_model:LiquidAI/LFM2.5-VL-3B-DSpark, base_model:quantized:LiquidAI/LFM2.5-VL-3B-DSpark, license:other, endpoints_compatible, region:us, conversational
- 作者：LiquidAI
- 发布时间：2026-09-24 22:54 CST
- 链接：https://huggingface.co/LiquidAI/LFM2.5-VL-3B-DSpark-GGUF

### 2. LiquidAI/LFM2.5-VL-3B-DSpark
- 摘要：image-text-to-text, sglang, safetensors, qwen3, speculative-decoding, dspark, lfm2, lfm2-vl, draft-model, arxiv:2603.14989, base_model:LiquidAI/LFM2.5-VL-3B, base_model:finetune:LiquidAI/LFM2.5-VL-3B, license:other, region:us
- 作者：LiquidAI
- 发布时间：2026-09-24 22:18 CST
- 链接：https://huggingface.co/LiquidAI/LFM2.5-VL-3B-DSpark

### 3. LiquidAI/LFM2.5-VL-3B
- 摘要：image-text-to-text, transformers, safetensors, lfm2_vl, liquid, lfm2.5, edge, conversational, custom_code, ar, zh, en, fr, de, hi, id, it, ja, ko, pl, pt, ru, es, th, vi, arxiv:2305.03393, base_model:LiquidAI/LFM2.5-2.6B-Base, base_model:finetune:LiquidAI/LFM2.5-2.6B-Base, license:other, endpoints_c...
- 作者：LiquidAI
- 发布时间：2026-09-24 22:11 CST
- 链接：https://huggingface.co/LiquidAI/LFM2.5-VL-3B

## Hugging Face Blog（huggingface-blog，en，本窗口共 2 条）

### 1. Accelerating vision-language models with LFM2.5-VL-DSpark
- 摘要：A Blog post by Liquid AI on Hugging Face
- 作者：Xx; Yuri Khrustalev; Leonie Monigatti; Viviana Márquez
- 发布时间：2026-09-24 22:08 CST
- 链接：https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark

### 2. How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning Workflows
- 摘要：A Blog post by NVIDIA on Hugging Face
- 作者：Johnny Nuñez Cano; Asier Arranz; Rishabh Chadha; Ben Oliveri
- 发布时间：2026-09-24 02:41 CST
- 链接：https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp

## Engineering at Meta（meta-engineering，en，本窗口共 1 条）

### 1. Bringing Private Processing to Meta AI Glasses
- 摘要：We believe glasses are the best form factor for having AI help throughout your day. They can understand your personal context better than other kinds of devices and keep you present without picking up a mobile phone. Most of the time, glasses are helping you see well, protecting your eyes and comple...
- 作者：Pritam Shah; Oskar Linde
- 发布时间：2026-09-24 08:00 CST
- 链接：https://engineering.fb.com/2026/09/23/security/private-processing-meta-ai-glasses/

## Meta Newsroom（meta-newsroom，en，本窗口共 3 条）

### 1. New Features for Meta Ray-Ban Display
- 摘要：Today at Connect 2026, we shared updates to Meta Ray-Ban Display , including new features, online ordering, and an expansion into five new markets. Navigate Hands-Free Heads-up navigation is a feature consumers consistently tell us they love in our Meta Ray-Ban Display glasses, and we’re excited to...
- 作者：Facebook
- 发布时间：2026-09-23 19:53 CST
- 链接：https://about.fb.com/news/2026/09/new-features-for-meta-ray-ban-display-navigation-hologram/

### 2. Introducing Meta VR Glasses: A Cinema, Courtside Seat, and Workspace in Just 100 Grams
- 摘要：Meet Meta VR Glasses: our most advanced device yet, delivering a personal cinema, courtside seat, workspace, and gaming console, all in a pair of glasses that weighs about 100 grams — roughly the same as a deck of cards. Thanks to the breakthrough glasses form factor, there are no straps or heavy ha...
- 作者：Facebook
- 发布时间：2026-09-23 19:42 CST
- 链接：https://about.fb.com/news/2026/09/introducing-meta-vr-glasses-3d-movies-immersive-live-sports-100-grams/

### 3. Introducing Ray-Ban Meta Audio and More AI Glasses Styles
- 摘要：Today at Connect, we announced Ray-Ban Meta Audio, our first-ever audio glasses, and our biggest expansion of AI glasses yet through our partnership with EssilorLuxottica. We’re building AI glasses for everyone. By the end of the year, we’ll offer more than 100 different glasses options across Ray-B...
- 作者：Facebook
- 发布时间：2026-09-23 19:36 CST
- 链接：https://about.fb.com/news/2026/09/introducing-ray-ban-meta-audio-glasses-new-styles-plus-muse/

## NVIDIA Blog（nvidia-blog，en，本窗口共 2 条）

### 1. How Open Science Can Help Researchers Prepare for the Next Pandemic
- 摘要：When COVID-19 emerged, scientists had a crucial advantage: Decades of prior research on coronaviruses meant they understood the virus’ key proteins well enough to design vaccines in record time. The next pandemic may not offer the same head start. To help improve the odds, NVIDIA has joined a coalit...
- 作者：Anthony Costa
- 发布时间：2026-09-24 22:00 CST
- 链接：https://blogs.nvidia.com/blog/open-protein-dataset/

### 2. Contain the Chaos: ‘CONTROL Resonant’ Launches on GeForce NOW
- 摘要：A warped Manhattan is waiting in the cloud this week. Remedy Entertainment’s CONTROL Resonant brings Dylan Faden’s extraordinary abilities and a paranatural crisis to GeForce NOW at launch. With the release comes the final days of the CONTROL Resonant Ultimate Membership Bundle . Purchase a 12-month...
- 作者：GeForce NOW Community
- 发布时间：2026-09-24 21:00 CST
- 链接：https://blogs.nvidia.com/blog/geforce-now-thursday-control-resonant/

## NVIDIA Technical Blog（nvidia-developer，en，本窗口共 4 条）

### 1. Efficient MoE Training for Biological Foundation Models
- 摘要：As language models grow, scaling dense architectures becomes increasingly expensive. In a dense transformer, every token passes through every layer, so adding... As language models grow, scaling dense architectures becomes increasingly expensive. In a dense transformer, every token passes through ev...
- 作者：Michelle Horton
- 发布时间：2026-09-24 23:00 CST
- 链接：https://developer.nvidia.com/blog/efficient-moe-training-for-biological-foundation-models/

### 2. Introducing NV-Reason-CT Open 3D CT VLM for Radiologist Chain-of-Thought Reasoning
- 摘要：Radiology AI has made remarkable strides in detecting abnormalities across chest X-rays, pathology slides, and 2D scans. Yet one of the most clinically rich and... Radiology AI has made remarkable strides in detecting abnormalities across chest X-rays, pathology slides, and 2D scans. Yet one of the...
- 作者：Tanya Lenz
- 发布时间：2026-09-24 06:54 CST
- 链接：https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/

### 3. Validate GPU Cluster Readiness Before AI Workloads Land
- 摘要：A GPU cluster can pass every health check and still fail to run an AI workload. Even when every GPU, network link, and pod reports healthy, a 512-GPU training... A GPU cluster can pass every health check and still fail to run an AI workload. Even when every GPU, network link, and pod reports healthy...
- 作者：Michelle Horton
- 发布时间：2026-09-24 03:45 CST
- 链接：https://developer.nvidia.com/blog/validate-gpu-cluster-readiness-before-ai-workloads-land/

## OpenAI News（openai-news，en，本窗口共 6 条）

### 1. Harvey turns legal context into stronger drafts with GPT-6 Astra
- 摘要：GPT-6 Astra produces more structured, context-aware legal documents, freeing lawyers to focus on strategy.
- 发布时间：2026-09-23 20:00 CST
- 链接：https://openai.com/index/harvey-from-context-to-confidence-with-astra

### 2. How invideo improves color grading 3x with GPT‑6 Astra
- 摘要：With GPT‑6 Astra, invideo plans edits with greater precision, improves color correction and grading threefold, and produces 50 custom effects in one day.
- 发布时间：2026-09-23 20:00 CST
- 链接：https://openai.com/index/invideo-builds-with-gpt-6-astra

### 3. Sam Altman’s remarks at the United Nations Security Council
- 摘要：OpenAI CEO Sam Altman discusses AI safety, human control, and international cooperation in remarks to the United Nations Security Council.
- 发布时间：2026-09-23 20:00 CST
- 链接：https://openai.com/index/sam-altman-un-security-council-remarks

# Tier 2 — 专业媒体

## Ars Technica — AI（arstechnica-ai，en，本窗口共 8 条）

### 1. New Jersey fines data center $1.1M after drone pics expose 62 gas generators
- 摘要：This week, New Jersey ordered the operator of one of the East Coast’s largest planned data centers to pay a $1.1 million fine for secretly installing and operating gas generators in violation of the state’s Air Pollution Control Act. DataOne got hit with the fine after an investigation by The Guardi...
- 作者：Ashley Belanger
- 发布时间：2026-09-25 02:20 CST
- 链接：https://arstechnica.com/tech-policy/2026/09/new-jersey-fines-data-center-1-1m-after-satellite-pics-expose-62-gas-generators/

### 2. Google's first Suncatcher orbital data center test launches October 1
- 摘要：Google is taking its first step toward making Project Suncatcher a reality. Announced last year, Suncatcher is Google's "moonshot" effort to design orbital AI data centers, which AI boosters like Elon Musk and Jeff Bezos have pitched as an alternative to divisive terrestrial data centers . Google's...
- 作者：Ryan Whitwam
- 发布时间：2026-09-25 00:16 CST
- 链接：https://arstechnica.com/google/2026/09/googles-first-suncatcher-orbital-data-center-test-launches-october-1/

### 3. OpenAI agent “didn’t accept no for an answer” in Australian government breach
- 摘要：Australian Prime Minister Anthony Albanese said his government is investigating a June incident in which an OpenAI agent accessed "non-public files" from the country's online Medicare statistics portal. OpenAI said in a statement that "our models took actions we did not intend" in causing the breach...
- 作者：Kyle Orland
- 发布时间：2026-09-25 00:01 CST
- 链接：https://arstechnica.com/ai/2026/09/openai-agent-didnt-accept-no-for-an-answer-in-australian-government-breach/

## Axios（axios，en，本窗口共 8 条）

### 1. Trump and Xi's summit revives panda diplomacy
- 摘要：Chinese President Xi Jinping said Thursday during a visit with President Trump that China will send two pandas to Zoo Atlanta , calling them an "envoy of friendship." Why it matters: The fuzzy ambassadors have long been one of China's most beloved tools of soft power and could signal an attempt to c...
- 作者：Josephine Walker
- 发布时间：2026-09-25 00:29 CST
- 链接：https://www.axios.com/2026/09/24/xi-trump-panda-diplomacy-zoo-atlanta

### 2. Inside China's mind on AI
- 摘要：China is waging a much different war for AI supremacy than the U.S. Why it matters: China is obsessed with state control and adoption. Chinese officials are laser-focused on deep, widespread AI domestic use they can monitor and steer at every level of their economy. By contrast, America is obsessed...
- 作者：Jim VandeHei
- 发布时间：2026-09-24 17:30 CST
- 链接：https://www.axios.com/2026/09/24/china-ai-plan-trump-xi-visit

### 3. Scoop: Trump allies open new front on Anthropic CEO as face of AI "doomerism"
- 摘要：President Trump's allies are targeting Anthropic CEO Dario Amodei as the face of AI "doomerism" and a founding father of the effective altruism movement that's come under increasing political fire. Why it matters: The attacks signal that Anthropic could remain a Trump target as his allies push back...
- 作者：Marc Caputo
- 发布时间：2026-09-24 17:00 CST
- 链接：https://www.axios.com/2026/09/24/trump-anthropic-ai-doomerism-dario-amodei

## Bloomberg Technology（bloomberg-tech，en，本窗口共 38 条）

### 1. AI Policy An Opportunity For 'Bipartisan Step Forward,' Says Miriam Vogel
- 摘要：Miriam Vogel, president and CEO of EqualAI, said that she heard very little partisan rhetoric when she testified on the impact of AI in front of lawmakers and described the creation of AI policy as an 'opportunity for a bipartisan step forward.' Vogel also weighed in on the AI race between the US an...
- 发布时间：2026-09-25 02:55 CST
- 链接：https://www.bloomberg.com/news/videos/2026-09-24/ai-an-opportunity-for-bipartisan-step-forward-vogel-video

### 2. AI Takes Center Stage From Oracle to the White House
- 摘要：Bloomberg’s Ed Ludlow breaks down Oracle's latest move to protect itself from mounting costs on a massive New Mexico data center facing regulatory setbacks and local opposition. Plus, Meta comes out with a new palm-sized device for using its popular new AI assistant, Muse; and all eyes are on Presid...
- 发布时间：2026-09-25 02:35 CST
- 链接：https://www.bloomberg.com/news/videos/2026-09-24/bloomberg-tech-9-24-2026-video

### 3. Darktrace CEO: AI Agents Are the New ‘Insider Threat’
- 摘要：Darktrace CEO Ed Jennings says AI agents are becoming a new kind of “insider threat” as companies rapidly deploy autonomous systems with access to sensitive data and infrastructure. As Darktrace launches new tools to track shadow AI, agent identities and behavior, Jennings discusses why cybersecurit...
- 发布时间：2026-09-25 02:32 CST
- 链接：https://www.bloomberg.com/news/videos/2026-09-24/darktrace-ceo-ai-agents-are-the-new-insider-threat-video

## CNBC Technology（cnbc-tech，en，本窗口共 8 条）

### 1. Palo Alto CEO says slowing down AI is ‘unrealistic’, extinction threat ‘extremely small’
- 摘要：Palo Alto CEO Nikesh Arora's views chime closely with Nvidia CEO Jensen Huang who has a diverging opinion to the bosses of Anthropic and OpenAI.
- 作者：Arjun Kharpal
- 发布时间：2026-09-24 20:24 CST
- 链接：https://www.cnbc.com/2026/09/24/palo-alto-networks-nikesh-arora-ai-slowdown.html

### 2. Cyber startup Island hits $6.4 billion valuation in new round as AI attacks fuel spending wave
- 摘要：Island faces an increasingly competitive cybersecurity market fueled by demand for agentic Ai defenses
- 作者：Samantha Subin
- 发布时间：2026-09-24 18:00 CST
- 链接：https://www.cnbc.com/2026/09/24/island-ai-cybersecurity-funding.html

### 3. OpenAI says agent hacked Australian government website without being told to do so
- 摘要：An OpenAI agent gained unauthorized access to an Australian government website while attempting to gather health data.
- 作者：Jenny Lee
- 发布时间：2026-09-24 12:34 CST
- 链接：https://www.cnbc.com/2026/09/24/openai-agent-hacked-australian-government-website-.html

## Financial Times — Technology（ft-tech，en，本窗口共 14 条）

### 1. Goldman reaped more than $200mn in fees from hedge fund Situational Awareness
- 摘要：Barely two-year-old AI-focused investment firm became biggest client of Wall Street bank’s prime brokerage unit
- 发布时间：2026-09-25 02:00 CST
- 链接：https://www.ft.com/content/bdec4129-ccac-4149-aa53-90ddd50cb925?syn-25a6b1a6=1

### 2. The AI agent revolution has moved a big step closer
- 摘要：Launch of Muse by Meta has provided a glimpse of how the technology could be turned into a mass-market product
- 发布时间：2026-09-25 01:33 CST
- 链接：https://www.ft.com/content/e60b40b6-dae5-4ccf-83cc-978269cbcaa5?syn-25a6b1a6=1

### 3. Beyond the AI abundance delusion
- 摘要：Concerns about inequality are likely to increase rather than decline as the technology transforms our societies
- 发布时间：2026-09-24 22:36 CST
- 链接：https://www.ft.com/content/fc521dcf-ee32-4c9c-b157-48e37d300943?syn-25a6b1a6=1

## The Guardian — AI（guardian-ai，en，本窗口共 20 条）

### 1. Launch of UK’s ‘largest AI supercomputer’ delayed by power supply problems
- 摘要：Datacentre hailed by government was supposed to start operating next year but may be held back into mid-2030s A huge datacentre project hailed by the UK government will miss its launch date next year and could be delayed into the mid-2030s. The site in Loughton, Essex, was described as the country’s...
- 作者：Dan Milmo Global technology editor
- 发布时间：2026-09-25 01:26 CST
- 链接：https://www.theguardian.com/technology/2026/sep/24/construction-largest-supercomputer-delayed

### 2. Rogue AI hacks government system for first time - The Latest
- 摘要：A government database has been hacked for the first time by a rogue OpenAI agent, which infiltrated part of the Australian healthcare scheme in June. OpenAI became aware of the hack in August, but only informed the government in September. Australia’s prime minister, Anthony Albanese, has expressed...
- 作者：Presented by Lucy Hough with Robert Booth ; produced by Angus Neale ; senior pro...
- 发布时间：2026-09-25 01:14 CST
- 链接：https://www.theguardian.com/news/video/2026/sep/24/rogue-ai-hacks-government-system-for-first-time-the-latest

### 3. Ben Jennings on smart glasses and AI hacks – cartoon
- 摘要：Continue reading...
- 作者：Ben Jennings
- 发布时间：2026-09-25 00:25 CST
- 链接：https://www.theguardian.com/commentisfree/picture/2026/sep/24/ben-jennings-smart-glasses-ai-hacks-cartoon

## Latent Space（latent-space，en，本窗口共 2 条）

### 1. Foundries vs Navigators: Lowering the Cost of Science
- 摘要：What does the future of science look like in the world of AI? Anthropic has some lofty goals for science and is even opening a wet lab . Meanwhile a quiet transformation 1 is happening all across AI x Science. In this guest post, Adrian Sanborn talks about the less flashy but more immediate ways he...
- 作者：Adrian Sanborn
- 发布时间：2026-09-24 23:03 CST
- 链接：https://www.latent.space/p/foundries-vs-navigators-lowering

### 2. [AINews] Meta Connect 2026: Muse glasses, voice, video, and Charm
- 摘要：Team Zuck is absolutely on fire. Here’s a good supercut of Meta Connect: and the effusive praise on Stratechery shows the mood on the ground. Unfortunately, no MSL updates beyond a tease , since Muse Spark was launched 3 weeks ago . However, Muse itself counts as a success, since it has overtaken Ch...
- 作者：Latent Space
- 发布时间：2026-09-24 16:12 CST
- 链接：https://www.latent.space/p/ainews-meta-connect-2026-muse-glasses

## MarkTechPost（marktechpost，en，本窗口共 4 条）

### 1. BottleCap AI Releases ThinkingCap-Qwen3.8-27B: 37.2% Fewer Thinking Tokens at a 0.86pp Accuracy Cost
- 摘要：BottleCap AI has released ThinkingCap-Qwen3.8-27B , the second model in its ThinkingCap series. It is a fine-tune of the Qwen team’s Qwen3.8-27B with one narrow goal: shorter reasoning traces. Across 12 benchmarks, it spends 37.2% fewer thinking tokens on average. Macro-average accuracy moves from 8...
- 作者：Michal Sutter
- 发布时间：2026-09-25 02:58 CST
- 链接：https://www.marktechpost.com/2026/09/24/bottlecap-ai-releases-thinkingcap-qwen3-8-27b-37-2-fewer-thinking-tokens-at-a-0-86pp-accuracy-cost/

### 2. Contrastive-LM Releases CLM-8B: An Open System One Model That Scores Agent Actions Up to 9× Faster Than Jev
- 摘要：Contrastive-LM has released CLM-8B , the first open model in a new class called Contrastive Language Models (CLMs). CLM does not generate text. It scores a set of candidate actions against the current state and returns probabilities. Their main baseline is Jev , the proprietary System One model from...
- 作者：Michal Sutter
- 发布时间：2026-09-24 13:27 CST
- 链接：https://www.marktechpost.com/2026/09/23/contrastive-lm-releases-clm-8b-an-open-system-one-model-that-scores-agent-actions-up-to-9x-faster-than-jev/

### 3. A Coding Guide to TypeSafe AI Jev: Typed Decisions, Calibrated Confidence, and Speculative Fan-Out with a System One Model
- 摘要：In this tutorial , we work with Jev , TypeSafe AI’s first System One model, which does not generate text at all: we send it a piece of program state and a set of typed questions, and it returns choices, scores, and yes/no probabilities that our code can branch on directly. We install the official Py...
- 作者：Asif Razzaq
- 发布时间：2026-09-24 08:53 CST
- 链接：https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/

## MIT Technology Review — AI（mit-tech-review，en，本窗口共 1 条）

### 1. The AI Hype Index: AI loves cheating
- 摘要：Brace yourself: It turns out AI is being optimized for cheating. OpenAI’s agents hacked into Hugging Face to get the answers to a cybersecurity test. Next, they solved a prestigious math problem (or just stole from two top mathematicians’ answer sheets). Anthropic’s models have also hacked into othe...
- 作者：Michelle Kim
- 发布时间：2026-09-23 17:00 CST
- 链接：https://www.technologyreview.com/2026/09/23/1144940/ai-hype-index-ai-loves-cheating/

## Nature — Machine Learning（nature-ml，en，本窗口共 7 条）

### 1. Optimizing the delivery of radiotherapy with artificial intelligence
- 发布时间：2026-09-24 08:00 CST
- 链接：https://www.nature.com/articles/s41571-026-01204-4

### 2. ResolVI: addressing noise and bias in spatial transcriptomics
- 发布时间：2026-09-24 08:00 CST
- 链接：https://www.nature.com/articles/s41592-026-03212-9

### 3. UpTCR: a unified progressive knowledge transfer foundation model for robust T-cell receptor-antigen binding recognition
- 发布时间：2026-09-24 08:00 CST
- 链接：https://www.nature.com/articles/s41467-026-78075-x

## New York Times — Technology（nyt-tech，en，本窗口共 5 条）

### 1. Google Is Sending an A.I. Data Center to Outer Space
- 摘要：A technician in a clean room at the Planet Labs office inspects the solar panels and wires of a Google-commissioned satellite before a vibration test meant to mimic the shaking it will undergo during launch.
- 作者：Kate Conger and Cade Metz
- 发布时间：2026-09-24 21:48 CST
- 链接：https://www.nytimes.com/2026/09/24/technology/google-suncatcher-ai-data-center-space.html

### 2. OpenAI’s A.I. Tried Breaching Four Other Targets, With No Prompting
- 摘要：OpenAI’s offices in San Francisco. At least four times this year, the company’s artificial intelligence hacked or tried to break into government and university websites without being instructed to do so.
- 作者：Kate Conger and Victoria Kim
- 发布时间：2026-09-24 10:50 CST
- 链接：https://www.nytimes.com/2026/09/23/technology/openai-ai-breach-australia.html

### 3. Meta Unveils 3 Smart Glasses With Built-In A.I.
- 摘要：Mark Zuckerberg, Meta’s chief executive, at the company’s developer conference on Wednesday.
- 作者：Eli Tan
- 发布时间：2026-09-24 08:16 CST
- 链接：https://www.nytimes.com/2026/09/23/technology/meta-ai-smart-glasses-conference.html

## SemiAnalysis（semianalysis，en，本窗口共 1 条）

### 1. ClusterMAX 3.0: The Industry Standard GPU Cloud Rating System Returns
- 摘要：This post has bonus content for paid subscribers. Upgrade to get full access. In 8 months since our last major release of ClusterMAX, slavering investors have just about run out of pockets to stuff checks into. GPU supply has gone to zero. Meanwhile, we have been hard at work putting clusters throug...
- 作者：Jordan Nanos
- 发布时间：2026-09-24 05:20 CST
- 链接：https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard

## Simon Willison's Weblog（simon-willison，en，本窗口共 2 条）

### 1. Gemini 3.8 TTS Playground
- 摘要：Tool: Gemini 3.8 TTS Playground Google released two new Gemini text-to-speech models today - gemini-3.8-flash-tts and gemini-3.8-flash-lite-tts . They come with a library of over 2,000 voices, plus the ability to create a custom voice with "just a 30-second audio sample of your voice or a voice you...
- 作者：Simon Willison
- 发布时间：2026-09-24 01:12 CST
- 链接：https://simonwillison.net/2026/Sep/23/gemini-tts-playground/

### 2. Shadow roots, explained with live examples
- 摘要：Tool: Shadow roots, explained with live examples Prompt to Fable 5.1 Medium: Build an artifact to explain shadow roots in CSS with interactive examples Tags: css
- 作者：Simon Willison
- 发布时间：2026-09-24 00:37 CST
- 链接：https://simonwillison.net/2026/Sep/23/shadow-roots/

## TechCrunch — AI（techcrunch-ai，en，本窗口共 21 条）

### 1. Bring your co-founder, partner, or colleague and get 50% off a second TechCrunch Disrupt 2026 pass
- 摘要：Buy one pass to TechCrunch Disrupt 2026 and get 50% off a second of the same ticket type. Register before event starts on October 13 at 8 a.m. PT.
- 作者：TechCrunch Events
- 发布时间：2026-09-25 03:15 CST
- 链接：https://techcrunch.com/2026/09/24/bring-your-co-founder-partner-or-colleague-and-get-50-off-a-second-techcrunch-disrupt-2026-pass/

### 2. PrismML brings its tiny LLMs to Qualcomm-powered smart glasses
- 摘要：Prism's larger goal is open-weight AI that runs on devices and makes better use of the computing power they already have.
- 作者：Julie Bort
- 发布时间：2026-09-25 03:00 CST
- 链接：https://techcrunch.com/2026/09/24/prismml-brings-its-tiny-llms-to-qualcomm-powered-smart-glasses/

### 3. Oracle sends force majeure notice on its New Mexico Stargate data center
- 摘要：The notice would allow Oracle to delay payments should the facility miss its 2028 target to come online.
- 作者：Aditya Mehta
- 发布时间：2026-09-25 02:11 CST
- 链接：https://techcrunch.com/2026/09/24/oracle-sends-force-majeure-notice-on-its-new-mexico-stargate-data-center/

## The Decoder（the-decoder，en，本窗口共 12 条）

### 1. Top AI experts badly underestimated how fast the field is moving, study finds
- 摘要：Leading AI experts have consistently underestimated how fast AI is advancing, according to the Forecasting Research Institute. AI reached gold-medal level at the International Mathematical Olympiad five years ahead of the median expert forecast, and Anthropic's annualized revenue is about five times...
- 作者：Matthias Bastian
- 发布时间：2026-09-25 03:18 CST
- 链接：https://the-decoder.com/top-ai-experts-badly-underestimated-how-fast-the-field-is-moving-study-finds/

### 2. Sakana AI hires Jürgen Schmidhuber, inventor of deep learning, world models, and your next ChatGPT update
- 摘要：Tokyo-based Sakana AI has hired Jürgen Schmidhuber as Chief Scientific Advisor. Sakana calls him the "father of modern AI." He'll help lead the company's new RSI Lab, which works on recursive self-improvement, meaning AI that keeps developing itself. His ideas from the 1990s have already shaped Saka...
- 作者：Matthias Bastian
- 发布时间：2026-09-25 02:06 CST
- 链接：https://the-decoder.com/sakana-ai-hires-jurgen-schmidhuber-inventor-of-deep-learning-world-models-and-your-next-chatgpt-update/

### 3. Google's Suncatcher project aims to put AI data centers in orbit powered by solar energy
- 摘要：Google's "Suncatcher" project aims to run AI infrastructure in orbit on solar power. A fridge-sized experimental satellite is set to launch on a SpaceX Falcon 9 on October 1. But the challenges are steep: you'd need around 10,000 satellites to match a single 1-gigawatt data center on Earth, and Jeff...
- 作者：Matthias Bastian
- 发布时间：2026-09-25 01:45 CST
- 链接：https://the-decoder.com/googles-suncatcher-project-aims-to-put-ai-data-centers-in-orbit-powered-by-solar-energy/

## The Verge — AI（theverge-ai，en，本窗口共 23 条）

### 1. Jensen Huang talks about AI and climate change like a supervillain
- 摘要：As Jensen Huang puts it, AI can help fight climate change - but only if it inflicts "an enormous amount of pain and suffering" first. The Nvidia CEO discussed the future of energy and AI's impact on our planet in the latest episode of The Ezra Klein Show . But his comments boil down to the same acce...
- 作者：Justine Calma
- 发布时间：2026-09-25 02:04 CST
- 链接：https://www.theverge.com/tech/1000140/jensen-huang-nvidia-ai-energy-climate-change-supervillain

### 2. Meta is going to let you build games with AI right on your phone
- 摘要：Meta has a new plan to get people to make games for its Horizon social platform. The company today announced two new development tools that will let you create games with AI prompts: Horizon Create, a mobile app, and Horizon Studio, a browser app that offers more granular controls. The apps will be...
- 作者：Jay Peters
- 发布时间：2026-09-25 01:52 CST
- 链接：https://www.theverge.com/games/999972/meta-horizon-create-studio-ai-games

### 3. Muse will apparently let you download its entire filesystem
- 摘要：A pair of developers say that with very little prompting, Meta's Muse will share its entire filesystem with you. Peter James and Jonny L. Saunders have said they both independently coaxed Muse into zipping up and sharing the entire contents of its root filesystem, Ubuntu system files, app templates,...
- 作者：Terrence O’Brien
- 发布时间：2026-09-25 01:14 CST
- 链接：https://www.theverge.com/ai-artificial-intelligence/1000222/meta-muse-ai-filesystem

## TLDR AI（tldr-ai，en，本窗口共 1 条）

### 1. Gemini TTS 🗣️, Claude’s novel enzyme 🧬, Google private memory 🔒
- 摘要：Gemini TTS 🗣️, Claude’s novel enzyme 🧬, Google private memory 🔒
- 作者：TLDR
- 发布时间：2026-09-24 08:00 CST
- 链接：https://tldr.tech/ai/2026-09-24

## VentureBeat（venturebeat，en，本窗口共 2 条）

### 1. VibeOps tackles the governance challenge of enterprise vibe coding
- 摘要：Presented by Fabrix.ai Read more
- 发布时间：2026-09-25 00:00 CST
- 链接：https://venturebeat.com/orchestration/vibeops-tackles-the-governance-challenge-of-enterprise-vibe-coding

### 2. AI coding tools are accelerating dependency sprawl and expanding malware risk with it
- 摘要：Presented by Chainguard Read more
- 发布时间：2026-09-24 22:30 CST
- 链接：https://venturebeat.com/security/ai-coding-tools-are-accelerating-dependency-sprawl-and-expanding-malware-risk-with-it

## WIRED — AI（wired-ai，en，本窗口共 6 条）

### 1. Google’s Gemini Can Now Make Calls for You on Pixel Phones
- 摘要：Call for Me—a feature that’s exclusive to the Pixel 11 series—gives robocalls a new meaning.
- 作者：Julian Chokkattu
- 发布时间：2026-09-25 00:00 CST
- 链接：https://www.wired.com/story/googles-gemini-can-now-make-calls-for-you-on-pixel-phones/

### 2. An OpenAI Agent Hacked Australia’s Health Service. Their Government Found Out Months Later
- 摘要：The country’s prime minister expressed disappointment at being informed of the hack only via email. Now Australia is investigating whether OpenAI broke the law.
- 作者：Isabella Ward
- 发布时间：2026-09-24 18:46 CST
- 链接：https://www.wired.com/story/openai-agent-hacked-australias-health-service-their-government-found-out-months-later/

### 3. Meta VR Glasses, Ray-Ban Meta Audio, Ray-Ban Meta Gen 3: Specs, Features, Prices
- 摘要：At its Meta Connect event, CEO Mark Zuckerberg announced a handful of new smart glasses, including a slimmed-down VR headset and the company’s first camera-free glasses.
- 作者：Boone Ashworth
- 发布时间：2026-09-24 07:42 CST
- 链接：https://www.wired.com/story/metas-answer-to-the-meta-creep-camera-free-smart-glasses/

## 36氪 AI 频道（36kr-ai，zh，本窗口共 60 条）

### 1. 大厂的AI战火，攻入硬件
- 摘要：大厂的AI战火，从屏幕里的应用，烧向看得见摸得着的终端。 2023年“百模大战”后，这是大模型战争的第四个年头，过去，各家围绕参数、榜单和推理成本下了血本，最近，新的变化又始现。 9月22日，据《晚点LatePost》报道，继AI眼镜后，阿里云旗下无影团队正在试水一款QwenBook的AI平板设备，定位原生智能体电脑，完整版预计2026年年底或2027年年初发布。 在此前 ，字节刚推出第二代豆包手机，小米开源AI硬件项目，百度也升级了小度智能体。另外，今年上半年，华为更是一口气推出数款新品智能终端，其中首款鸿蒙AI眼镜成为其抢占增量入口的关键。 动作看似分散，实则指向一个趋势。那便是，当AI从...
- 作者：听筒Tech
- 发布时间：2026-09-24 20:57 CST
- 链接：https://www.36kr.com/p/3997256894977664

### 2. 宇树退烧之后，这家机器人企业花8亿买了一家装修公司
- 摘要：摘要：当IPO越来越看重一家机器人公司“已经做成了什么”，那些还在成长中的公司，可能开始思考——能不能先拥有一家上市公司，再等待自己的产业真正成熟？ 一边是成立不到两年的机器人创业公司，年收入还只有千万元级；另一边是成立42年、上市9年、如今已经被*ST、净资产为负的传统装修公司。现在，前者准备花8.1亿元，成为后者的新老板。 背后的问题是：在机器人企业IPO审核趋严的背景下，为什么突然出现机器人公司通过重组、并购、上市公司控制权等方式，进入资本市场？这究竟只是几起独立的资本运作，还是机器人公司正在尝试探索IPO之外的资本化路径？ 两个不相干的世界撞在了一起 很难想象，机器人公司和装修公司能有...
- 作者：凤凰网科技
- 发布时间：2026-09-24 20:54 CST
- 链接：https://www.36kr.com/p/3997354896969603

### 3. 三个印度人如何用AI建起一座4亿美元内容工厂
- 摘要：在AI技术辅助下，这家人气音频微短剧平台每月产出20万小时的用户生成内容。其中诞生了足够多的爆款，平台由此相信这就是娱乐业的未来。 在一个被外星战争蹂躏的反乌托邦世界里，一个在学校被欺凌的男孩发现了一本古老的书，那是他从未谋面的父母留下的。结果这本书把他变成了吸血鬼。这只是《我的吸血鬼系统》（My Vampire System）前10分钟的内容。该剧是Pocket FM上最受欢迎的音频剧，自四年前首播以来播放量已超过15亿次。故事后续还有4192集，剧情紧凑，悬念不断。如果你想全部听完，就得做好掏钱的准备了。 01 Pocket这家音频娱乐公司总部位于印度，几乎完全通过微交易赚钱。 用户每天可...
- 发布时间：2026-09-24 20:48 CST
- 链接：https://www.36kr.com/p/3997184622186372

## 36氪 快讯（36kr-newsflash，zh，本窗口共 19 条）

### 1. 美股大型科技股盘前普跌，美光科技跌超2%
- 摘要：36氪获悉，美股大型科技股盘前普跌，截至发稿，美光科技、英特尔、闪迪跌超2%，Meta、亚马逊、英伟达跌超1%，特斯拉跌0.97%，微软跌0.51%，谷歌跌0.31%，苹果跌0.02%。
- 发布时间：2026-09-24 20:53 CST
- 链接：https://www.36kr.com/newsflashes/3997408036638594

### 2. OpenAI智能体擅自访问医保数据 澳政府将调查
- 摘要：澳大利亚副总理理查德·马尔斯24日表示，美国开放人工智能研究中心（OpenAI）的一个智能体未经授权访问澳国民医疗保险体系数据门户的行为“完全不可接受”，政府将调查此事是否违反澳法律。马尔斯24日说，澳政府高度重视此事，已对OpenAI延迟通报表示关切。不过他也表示，事件影响相对有限。“涉及的是汇总医疗统计数据，没有任何个人的医疗数据被访问，系统本身也未遭到任何破坏。”马尔斯表示，澳方相关工作组将调查事件是否违反澳大利亚法律，并评估现行法律能否适应人工智能能力不断发展的形势。（新华社）
- 发布时间：2026-09-24 18:07 CST
- 链接：https://www.36kr.com/newsflashes/3997236649201537

### 3. 亨通光电：拟定增募资不超66.36亿元用于光通信及能源互联项目
- 摘要：36氪获悉，亨通光电公告，公司拟向特定对象发行A股股票，募集资金总额不超过66.36亿元，扣除发行费用后拟用于新一代光纤研发及生产项目、内蒙古光学高端光学新材料建设项目、CPO先进封装研发项目、亨通数据智联通信项目、AI先进光互联项目、亨通(揭阳)海洋能源互联与智慧运维项目、万吨级深远海敷设船投资建设项目、亨通智能制造产业基地项目及补充流动资金。本次发行对象为不超过35名特定投资者，发行价格不低于定价基准日前20个交易日股票交易均价的80%，发行数量不超过7.4亿股，即不超过发行前总股本的30%。
- 发布时间：2026-09-24 18:00 CST
- 链接：https://www.36kr.com/newsflashes/3997238094631041

## 极客公园（geekpark，zh，本窗口共 4 条）

### 1. Agent 时代来了，3D 生成大模型接下来比什么？
- 摘要：9 月 3 日，GPT-6 Astra 的发布，把 3D 内容创作带到了舞台中央。 在 GPT-6 Astra 官方发布页的一个不到 3 分钟的视频里与后续解读中，Astra 已经能直接进入 Blender，从一句住宅设计需求开始搭场景，先生成极简住宅，后来又将其扩展为围绕庭院展开的家庭住宅。里面有卧室、办公室、厨房和卫生间；家具从床板、衣柜挂杆、烤箱、餐具抽屉，再到灯光模拟，一应俱全。甚至水槽表面的法线出了问题之后，Astra 还会自己返工。 为了制作 30 秒室内漫游，它还会把相机放在约 1.65 米的人眼高度，用 24—26mm 镜头安排四段运动；进入 Unreal Engine 5 之...
- 作者：极客老友
- 发布时间：2026-09-24 22:49 CST
- 链接：http://www.geekpark.net/news/371031

### 2. 李彦宏的长期主义，进入回报周期
- 摘要：作者｜cola 编辑｜郑玄 9 月 21 日，百度创始人李彦宏在内部活动上为技术团队颁发「百度最高奖」。两支入围团队均获奖，各获 100 万美元奖励。 其中，天池团队面向万亿级 MoE 大模型，自主研发百度天池超节点架构；dodo 团队是通过打造企业 AI 员工。 它们代表着百度当下两条重要的技术探索：基于 昆仑芯 的天池超节点，向更大规模的 AI 基础设施深入；以及让 Agent 真正进入组织。 但如果把时间轴再往前拉，百度今天的 AI 故事，还有一条更早埋下的技术伏笔——昆仑芯。 2010 年前后，百度搜索业务的服务器集群规模随流量高速扩张，海外进口芯片单片成本高达上万美元，持续攀升的算力...
- 发布时间：2026-09-24 19:34 CST
- 链接：http://www.geekpark.net/news/371030

### 3. 从数人头到数智能体：一场正在发生的企业生产力换血
- 摘要：用了 AI、消耗了 Token，不一定就是 AI 原生组织，但不用肯定没有机会。 作者｜Li Yuan 编辑｜ 郑玄 先让许多管理者感到危险的，往往不是行业里又冒出了什么新技术概念，而是身边的同行突然拿出了完全看不懂的交付速度和报价单。 这种压迫感在今年变得极其具体：老牌企业正在把成群的智能体塞进核心生产线，甩掉繁琐的流程包袱；而那些从第一天起就生长在 AI 上的轻量团队，几个人就能直接撬动过去上千人公司的研发与交付产能。 当两拨底子完全不同的人在同一个市场里正面碰撞，企业间原有的体量界限正在被彻底击碎——竞争的胜负手不再取决于你积累了多少年的组织规模，而取决于业务链条上有多少比例被机器智能真...
- 作者：Li Yuan
- 发布时间：2026-09-24 16:13 CST
- 链接：http://www.geekpark.net/news/371011

## 虎嗅（huxiu，zh，本窗口共 37 条）

### 1. 一天做出产品，正在成为AI创业者最昂贵的幻觉
- 摘要：2024年，41岁的马修·加拉格尔坐在洛杉矶的家里，花了两个月和2万美元，启动了一家公司。这家公司叫Medvi，主营GLP-1减重药的远程医疗服务。AI替他写代码、做网站、生成广告素材、处理客服、分析经营数据。2025年，也就是Medvi第一个完整经营年度，它做出了4.01亿美元的销售额。此后，加拉格尔才聘请...... 本文来自微信公众号： 不懂经 ，作者：经叔，原文标题：《一天做出产品，正在成为AI创业者最昂贵的幻觉| 不懂经网站》 2024年，41岁的马修·加拉格尔坐在洛杉矶的家里，花了两个月和2万美元，启动了一家公司。 这家公司叫Medvi，主营GLP-1减重药的远程医疗服务。AI替他...
- 作者：不懂经©
- 发布时间：2026-09-24 23:40 CST
- 链接：https://www.huxiu.com/article/4893886.html

### 2. 《抓特务》口碑反转，冯小刚30年为什么总被延迟认可？| 拆解3292条短评
- 摘要：“好片，被人黑了。”“是有人带节奏吧，可惜了，这个片子。”8月28日，《抓特务》上线流媒体，腾讯视频的高赞评论里不乏遗憾之声，弹幕里，“欠冯导一张电影票”也时常飘过。上映两个月，《抓特务》仅有1.19亿票房，按照冯小刚透露，该影片成本1.65亿，并未回本。但上线流媒体第二天，《抓特务》腾讯视频最高热度1993...... 本文来自微信公众号： 娱乐资本论 ，作者：娱子酱团队，原文标题：《《抓特务》口碑反转，冯小刚30年为什么总被延迟认可？| 拆解3292条短评》 “好片，被人黑了。” “是有人带节奏吧，可惜了，这个片子。” 8月28日，《抓特务》上线流媒体，腾讯视频的高赞评论里不乏遗憾之声，弹...
- 作者：娱乐资本论
- 发布时间：2026-09-24 23:17 CST
- 链接：https://www.huxiu.com/article/4893883.html

### 3. 医保局下场办了场脑机接口大赛，透露什么信号？
- 摘要：在近日举行的“2026全球脑机接口×医保创新场景大赛”决赛上，共有251个项目在9类赛道展开角逐。“意念传书”脑控打字比赛区，选手头戴脑电采集设备，目光扫过屏幕上的虚拟键盘，字符被逐一“选中”输入。没有手指敲击，没有语音指令，仅凭注视完成输入。赛场上的技术很酷，但病房里的需求更为朴素。失去语言能力的渐冻症患者...... 本文来自微信公众号： 财联社 ，作者：武超 在近日举行的“2026全球脑机接口×医保创新场景大赛”决赛上，共有251个项目在9类赛道展开角逐。 “意念传书”脑控打字比赛区，选手头戴脑电采集设备，目光扫过屏幕上的虚拟键盘，字符被逐一“选中”输入。没有手指敲击，没有语音指令，仅凭...
- 作者：财联社©
- 发布时间：2026-09-24 21:25 CST
- 链接：https://www.huxiu.com/article/4893868.html

## 爱范儿（ifanr，zh，本窗口共 11 条）

### 1. 14.99 万元起，全新旅行者 7 开启预售，插混燃油两手抓
- 摘要：9 月 23 日，全新旅行者 7 正式开启预售。 作为换代车型，新车最直观的变化是换装了标志性圆灯前脸，车身小幅加长，并在保留硬朗方盒子轮廓的同时，全维升级了座舱舒适、高阶智驾硬件与插混电气架构。 旅行者 7 这次带来了燃油版和C-DM 插混版，一共推出 7 款车型： 燃油版： 1.5TD 探索+ 14.99 万元 2.0TD XWD 发现 15.99 万元 2.0TD XWD 穿越 16.99 万元 2.0TD XWD 征服 17.99 万元 C-DM 版： PRO 15.99 万元 MAX 16.99 万元 MAX+ 17.99 万元 所谓的 C-DM，也就是Chery Dual Mode...
- 作者：陈世琛
- 发布时间：2026-09-24 20:05 CST
- 链接：https://www.ifanr.com/1682158?utm_source=rss&utm_medium=rss&utm_campaign=

### 2. 奕境 X9 上市 28.98 万元起！华为系大六座有了一个新选项
- 摘要：9 月 24 日，奕境 X9 正式上市。 聊起这台车，你很难不把它跟问界 M9 联系在一起。 第一眼看去，奕境 X9 的视觉观感与问界 M9 有着高度相似，而在更深层的领域，奕境与问界都与华为有着很深的联系。 奕境是东风与华为乾崑共创的独立品牌，和问界类似，奕境 X9 也深度融入了华为的辅助驾驶、鸿蒙座舱与数字底盘技术。 但不一样的是，这台奕境 X9 在价格上可要低不少。 这一次奕境 X9 一共带来四款增程车型： 增程 Max 长续航：28.98 万元 增程 四驱 Ultra：29.98 万元 增程 四驱 Ultra+ 长续航：32.98 万元 增程 四驱 Ultra+ 旗舰 长续航：36.9...
- 作者：陈世琛
- 发布时间：2026-09-24 20:01 CST
- 链接：https://www.ifanr.com/1682142?utm_source=rss&utm_medium=rss&utm_campaign=

### 3. 1/3 价格，1/8 重量，Meta 新眼镜秒杀 Vision Pro 了？
- 摘要：从现在起，眼镜要为「超级智能」而打造。 在今早的 Meta Connect 2026 主题演讲上，扎克伯格公开了一系列 AI 硬件新品—— 没有摄像头的纯音频 AI 智能眼镜 Ray-Ban Meta Audio、仅 100 克的超轻 VR 眼镜 Meta VR Glasses，以及既有智能眼镜产品的更多造型与联名款。 类似的设备形态，指向了同一个目的： 要将「眼镜」打造成一种与 Meta 牢牢绑定的计算设备品类。 Ray-Ban Meta Audio：拿掉摄像头，换来全天候使用 为什么是眼镜？扎克伯格给出的解释是：世界上有约 20 亿人戴眼镜，并且眼镜不会像耳机一样将个人与外界隔绝，可以说是...
- 作者：彭海星
- 发布时间：2026-09-24 20:00 CST
- 链接：https://www.ifanr.com/1682116?utm_source=rss&utm_medium=rss&utm_campaign=

## InfoQ 中文（infoq-cn，zh，本窗口共 10 条）

### 1. 云栖之后，10+阿里AI实战派将亮相QCon上海站
- 摘要：点击查看原文>
- 作者：QCon全球软件开发大会
- 发布时间：2026-09-24 18:38 CST
- 链接：https://www.infoq.cn/article/lh6Z5E9Zkr33bOeHQGky?utm_source=rss&utm_medium=article

### 2. 世界人工智能开源大赛（GOAI）总决赛暨颁奖盛典在杭州举行
- 摘要：点击查看原文>
- 作者：世界人工智能开源大赛
- 发布时间：2026-09-24 18:11 CST
- 链接：https://www.infoq.cn/article/hrmb2p18iKEwl24OMvcv?utm_source=rss&utm_medium=article

### 3. WSO2 发布 Agent Manager，企业寻求应对日益严重的 AI Agent 泛滥问题
- 摘要：点击查看原文>
- 作者：作者：Craig Risi
- 发布时间：2026-09-24 17:25 CST
- 链接：https://www.infoq.cn/article/4gr5Zt9GZoyIwF2f6LvR?utm_source=rss&utm_medium=article

## IT之家（ithome，zh，本窗口共 99 条）

### 1. 华为乾崑智驾 ADS 5 系统 9 月版本更新亮点公布，升级 AR 人找车、实时对讲等功能
- 摘要：IT之家 9 月 25 日消息，华为乾崑智能汽车解决方案官方宣布，华为乾崑智驾 ADS 5 新版本（即 9 月 OTA 新版本）即将推送，领航 / 泊车体验双升级。新版本还升级了组队出行、导航搜索场景拓展等功能。 IT之家整理新版本更新内容（ ADS Max V5.0.2 ）如下： 领航体验 升级组队出行：支持创建 / 加入出行队伍，全员位置实时显示，防止走散更省心。支持一键跟随队长同步导航路线。 升级实时对讲：一键开启队内实时语音对讲，支持多人同时发言。既可随时分享沿途美景，也能提前预警拥堵路况。 升级导航搜索场景拓展：导航中搜索能力进阶，除沿途搜索外，新增自车周边、目的地两大搜索场景。 自...
- 作者：作者： 归泷
- 发布时间：2026-09-25 01:51 CST
- 链接：https://www.ithome.com/1/007/047.htm

### 2. 李楠谈锤子科技 TNT 生不逢时：有了 Agent 之后，这些操作其实都不是非常难
- 摘要：IT之家 9 月 24 日消息，Angry Miao 创始人、前魅族科技 CMO 李楠今天在微博发文称，锤子科技的 TNT 真是生不逢时。今天有了 Agent 之后，这些操作其实都不是非常难了。 据IT之家了解，锤子科技的坚果 TNT 工作站本质上是一块显示屏，它搭载 27 英寸 IPS 全贴合 4K 屏幕，支持十点触控，内置独立音频信号处理器，拥有“十大神钮”，可实现“高效便捷操作”。 罗永浩曾表示 ，他直到现在都认为，当年做 TNT 的决策没有错，而是错在资源不够。一台桌面级电脑里如果加上了多点触控和语音，就可以实现远比 PC 和 Mac 效率更高的工作，而且当年还有三星和华为去做了“手机...
- 作者：作者： 潞源
- 发布时间：2026-09-24 23:12 CST
- 链接：https://www.ithome.com/1/007/039.htm

### 3. 华为鸿蒙 HarmonyOS 7.0.0.109 SP6 版本开启推送，新增智能识别信息内容等功能
- 摘要：IT之家 9 月 24 日消息，华为鸿蒙 HarmonyOS 7.0.0.109 SP6 版本今日开启推送，首批面向 Mate 80 系列、Pura 90 系列、nova 16 系列等机型，系统包大小约 702.73MB。据介绍，本次更新优化了部分场景的显示效果，同时提升了整机系统稳定性。 ▲ IT之家开箱：华为 Mate 80 Pro Max 风驰版图赏 IT之家附新版本更新内容如下： 信息 智能识别信息内容 ，挪车提醒、候补车票成功等信息可通过实况窗展示，提醒更及时 关怀和无障碍 文本通话支持声音修复，当发音不清晰时，使用该功能可让对方听得更清晰，轻松实现无障碍沟通（设置 > 关怀和无障碍...
- 作者：作者： 归泷
- 发布时间：2026-09-24 22:51 CST
- 链接：https://www.ithome.com/1/007/033.htm

## 雷峰网（leiphone，zh，本窗口共 12 条）

### 1. 现在不买带线控底盘的车，三年后注定会后悔
- 摘要：如果要找出2026年车市升温最快的技术赛道，线控底盘一定算一个。 此前在2024年，线控转向首次在量产车上出现，当时行业里的共识是：好东西，但离普通人太远。 2026年7月1日，由上汽集团牵头制定的线控转向国家标准《汽车转向系基本要求》（GB17675-2025）正式实施，政策闸门打开。 2026年9月16日，理想i9上市，线控转向加后轮转向标配。李想专门在微博上谈起这两项配置，他的思考是，大空间与好操控，需要靠技术进步同时实现，不能一直依赖把车做大。线控转向和后轮转向，正是理想为改善体验投入的方向。 由此可见，普及线控底盘，正在成为行业共识。 9月23日，全新一代智己LS6上市，19.79万...
- 发布时间：2026-09-24 18:42 CST
- 链接：https://www.leiphone.com/category/transportation/htudSUNPncuLmMfb.html

### 2. 腾势Z9S正式上市：纯电续航1100km，25.58万元起
- 摘要：9月23日，腾势旗下“科技豪华智能轿车”Z9S正式上市，推出闪充尊荣型、闪充旗舰型、易三方闪充性能型三款车型，面向用户“悦己、悦人、悦非凡”的不同需求。新车搭载第二代刀片电池及闪充技术，CLTC纯电续航最高1100km，官方给出“5分钟充好，9分钟充饱，零下30度只多3分钟”的补能表现。同时，易三方、AI超级智能体迪迪虾、Diva智能伙伴、天神之眼5.0及云辇-A智能空气车身控制系统等技术集中上车。腾势希望通过舒适、续航、驾控和智能四个维度的升级，重构豪华新能源轿车的价值标尺。 腾势Z9S官方指导价为25.58万元-32.58万元。上市同时，腾势推出十一重专属礼遇，官方公布的权益价值至高8万元...
- 发布时间：2026-09-24 18:30 CST
- 链接：https://www.leiphone.com/category/transportation/nBAYRoWBOZSuBT5D.html

### 3. 聚焦院外管理提质增效｜《急性冠状动脉综合征患者院外长期随访管理共识》更新研讨，胸痛中心智慧全程管理行动项目正式启动
- 摘要：近日，第八届“儒道心学”心血管病学会议、第十届沪鲁心血管病专家论坛、第九届日照心血管峰会在山东日照召开。由葛均波院士领衔，黄恺、苏国海、李春洁等数十位心血管领域权威专家参与，会上完成两大核心动作：一是召开《急性冠状动脉综合征患者院外长期随访管理共识》更新研讨会，专家集体锚定共识修订的核心方向；二是胸痛中心智慧全程管理行动项目正式启动，以专家共识为指引推进先行落地验证。作为医疗 AI 赋能院外管理创新的先行者，讯飞医疗执行总裁鹿晓亮受邀参会，与学界、业界共同推动心血管院外管理向标准化、智能化、全周期阶段迈进。 院外管理破局，从“患者参与”到“AI赋能” 历经十五年胸痛中心建设，我国急性心梗院内死...
- 发布时间：2026-09-24 18:03 CST
- 链接：https://www.leiphone.com/category/industrynews/5c353eBnBL6ShdzV.html

## 开源中国（oschina，zh，本窗口共 13 条）

### 1. 龙蜥社区SkillHub：Workshop实战、云栖颁奖、推荐系统发布，三箭齐发
- 摘要：AI原生操作系统正在从概念走向落地，而Skill生态的繁荣程度，将决定这一代操作系统能否真正支撑起智能体的规模化运行。今年开放原子开源生态大会上，龙蜥社区正式升级为AI原生操作系统社区，同期发布社区级技能生态平台SkillHub——这是龙蜥对“操作系统如何承载AI能力”这一产业命题给出的基础设施答案。两个月来，数百...
- 发布时间：2026-09-24 18:27 CST
- 链接：https://www.oschina.net/news/502739

### 2. 龙蜥社区SkillHub推荐系统正式发布，首批技能生态奖项揭晓
- 摘要：9月23日，在2026云栖大会“AI Agent原生操作系统”分论坛上，龙蜥社区正式发布SkillHub推荐系统并举行颁奖仪式。阿里云智能集团研发副总裁、龙蜥社区理事长马涛，中兴通讯副总裁、龙蜥社区副理事长刘东，AMD全球副总裁Raghu Nambiar等嘉宾共同出席，标志着龙蜥社区SkillHub从技能汇聚走向质量评测与榜单推荐。 对AI原生操...
- 发布时间：2026-09-24 18:03 CST
- 链接：https://www.oschina.net/news/502738

### 3. 小米公开 MiMo-V3 核心架构 HySparse2：KV 共享升两级、Prefill 少跑一半
- 摘要：小米 MiMo 团队负责人罗福莉（Fuli Luo）在 X 上预告了 MiMo-V3 的新推理架构 HySparse2，随后小米官方公众号也放出了完整介绍。面向长程多轮 Agent，这套方案的三个目标很直接：更少的 Prefill 计算、更小的 KV Cache、更精准的长上下文检索。 和 MiMo-V2.6 的 Hybrid SWA 相比，相对收益的系数是现成的：在百万 token ...
- 发布时间：2026-09-24 16:50 CST
- 链接：https://www.oschina.net/news/502736

## 量子位（qbitai，zh，本窗口共 11 条）

### 1. 出海Agent“小元AI”入驻腾讯WorkBuddy：找买家写开发信谈生意
- 摘要：懂出海，能记忆，自进化
- 作者：思邈
- 发布时间：2026-09-24 22:20 CST
- 链接：https://www.qbitai.com/2026/09/496961.html

### 2. PCIe显卡被低估了！内核补齐+通信重构，DeepSeek推理吞吐翻近7倍
- 摘要：1.5台6000D跑赢1台B300！
- 作者：思邈
- 发布时间：2026-09-24 22:17 CST
- 链接：https://www.qbitai.com/2026/09/496925.html

### 3. 时隔十年，AI大牛署名新论文
- 摘要：让自动驾驶“走一步想十步”
- 作者：杰西卡
- 发布时间：2026-09-24 20:58 CST
- 链接：https://www.qbitai.com/2026/09/496834.html

## 少数派（sspai，zh，本窗口共 1 条）

### 1. 派早报：小米召开秋季新品发布会、千问发布 Qwen-Audio-3.1系列模型等
- 摘要：Amazfit 推出智能手表 T-Rex Dual Solar、雷蛇推出灰鲭鲨 X 游戏音箱等。 查看全文
- 作者：少数派编辑部
- 发布时间：2026-09-24 08:19 CST
- 链接：https://sspai.com/post/114913

## 钛媒体（tmtpost，zh，本窗口共 31 条）

### 1. 具身智能的行业信用正在被机器人公司透支
- 摘要：9月24日，梅卡曼德（09615.HK）交出上市后的第一份中期账本，这距离它9月1日挂牌仅过了23天。而成立十年的梅卡曼德，此前积攒的行业热度，可能都不及最近这23天。 这份热度的来源，一是火热的IPO本身：公开发售获得3835倍认购，引来25.25万份申请，一手中签率3%；另一个来源，就是创始人邵天兰在上市后连续的“仗义掀桌式”发言，给具身智能行业当头下了一剂降火的猛药。 “他实在压抑得太久了”，有投资人这么评价邵天兰，“如果没有具身智能这波浪潮，梅卡曼德还不知道何时才能熬出头。” 直到2024年，梅卡曼德的自我定位还是“AI+工业 机器人 ”，而在2025年8月，它给市场讲的故事变成了“具...
- 作者：科技不焦虑
- 发布时间：2026-09-24 22:19 CST
- 链接：https://www.tmtpost.com/8152223.html

### 2. 构建全媒体安全体系，共建安全实验室！北京日报社与奇安信达成战略合作
- 摘要：9月24日，北京日报社与奇安信科技集团股份有限公司举行战略合作签约仪式。后续，双方将发挥主流媒体传播优势与网络安全技术优势，围绕媒体数字化转型、网络安全保障、安全科普、人才培养等方面开展全方位深度合作，协同构建全媒体全场景安全保障体系，联合共建网络安全创新实验室，合力打造权威媒体网络安全与数字化合规建设标杆。 北京日报社旗下拥有报刊、网站、客户端及近300个新媒体账号，已形成强大传播矩阵，是首都地区乃至全国最具影响力的主流媒体之一。奇安信集团是国内领先的网络安全厂商，具备重大活动网络安全保障实战经验，安全技术广泛应用于多行业数字化、智能化场景。 双方通过此次“握手”，将协同构建全媒体全场景安全...
- 作者：北京日报
- 发布时间：2026-09-24 21:56 CST
- 链接：https://www.tmtpost.com/8152228.html

### 3. 月内官宣74万吨扩产项目，锂电负极真的不够用了吗？｜行业风向标
- 摘要：（图片系AI生成） 锂电负极新一轮扩产潮，正席卷而来。 9月22日、23日， 科达制造 （600499.SH）、 杉杉股份 （600884.SH）接力抛出重磅扩产公告，两项目均落地内蒙古包头，投资额合计高达96亿元，新增产能达到65万吨。若叠加一周前 翔丰华 （300890.SZ）刚公告的拟在四川遂宁落地年产9.3万吨的新能源电池负极材料项目，三家A股上市公司合计官宣74.3万吨新增产能，合计拟投金额超109亿元。 将时间线拉长， 中科电气 （300035.SZ）、 尚太科技 （001301.SZ）、滨海新能（000695.SZ）等更多公司扩产已经官宣，超百万吨级的负极项目储备已在路上。 需要...
- 作者：价值刻度
- 发布时间：2026-09-24 20:03 CST
- 链接：https://www.tmtpost.com/8152117.html

## 智东西（zhidx，zh，本窗口共 12 条）

### 1. 实时世界模型竟然能这么玩？PixVerse R2登上Twitter热榜
- 摘要：智东西 作者 | 毕伟豪 编辑｜漠影 近日，一款 实时世界模型 在海外走红，9月22日上线当天就登上了X（Twitter）趋势榜第二。 它为什么会引发这么大的关注？ 有海外网友认为，这款模型带来的变化，是让AI生成 从“创作视频”转向“与AI世界互动” 。 还有网友称赞这不像是看视频，更像是 身临其境 。 这就是 爱诗科技（AIsphere） 最新发布的实时世界模型——PixVerse R2所呈现的效果，在PixVerse R2创造的世界中，用户可以移动、说话，做出选择。 用户输入的每一个提示词、做出的每一个动作，都会实时改变眼前的场景，甚至让剧情走向不同的方向。 回过头来看，AI诞生以来，世...
- 作者：毕 伟豪
- 发布时间：2026-09-24 16:51 CST
- 链接：https://zhidx.com/p/597184.html

### 2. DeepSeek被曝冲刺5000亿元估值！年化营收达67亿
- 摘要：智东西 作者 | 江宇 编辑 | 李水青 智东西9月24日消息，据外媒The Information今日报道，两名直接知情人士透露， DeepSeek目前的年化营收运行率已经达到10亿美元（约合人民币67.13亿元） ，较几个月前不足5亿美元的水平翻了一倍以上。 这一最新数据被曝是由DeepSeek创始人兼CEO梁文锋在近期一次投资者会议上披露 。近期模型涨价叠加持续增长的市场需求，共同推动了DeepSeek营收提升。 与此同时，据The Information报道，DeepSeek正在敲定新一轮融资， 计划最晚于今年10月底完成新一轮500亿元人民币融资 ， 目标估值为5000亿元人民币 。...
- 作者：江 宇
- 发布时间：2026-09-24 15:14 CST
- 链接：https://zhidx.com/p/597339.html

### 3. 口语转录，一步到位！全国产算力语音识别模型，听得懂上下文了
- 摘要：智东西 作者 | 杨京丽 编辑 | 李水青 智东西9月24日报道，昨日，科大讯飞推出最新 语音识别大模型Spark-ASR-2.0 。该模型基于 讯飞语音基座大模型Spark-Audio-1.0-Preview 构建，重点提升 通用识别、复杂声学场景识别、上下文识别和文本流畅规范性 。 值得注意的是，语音基座大模型Spark-Audio-1.0-Preview和语音识别模型Spark-ASR-2.0均 基于全国产算力展开训练 。讯飞正在以多年积累的智能语音技术和国产算力平台大模型训练经验为基础，持续推进语音基座模型、专用模型等技术迭代。 尽管大多数语音识别模型在日常使用中基本能够准确转写，但在...
- 作者：杨 京丽
- 发布时间：2026-09-24 15:02 CST
- 链接：https://zhidx.com/p/597300.html

# Tier 3 — 社交 / 聚合

## GitHub Trending (daily)（github-trending，en，本窗口共 7 条）

### 1. obra/superpowers
- 摘要：An agentic skills framework & software development methodology that works. Superpowers Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them. Table of Contents Ho...
- 发布时间：2026-09-24 18:16 CST
- 链接：https://github.com/obra/superpowers

### 2. strands-agents/harness-sdk
- 摘要：Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud. http://strandsagents.com/ Strands Agents A model-driven approach to building AI agents in just a few lines of code. Documentation ◆ Samples ◆ MCP Server ◆ Discord...
- 发布时间：2026-09-24 18:16 CST
- 链接：https://github.com/strands-agents/harness-sdk

### 3. HKUDS/CLI-Anything
- 摘要："CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ https://clianything.cc/ CLI-Anything: Making ALL Software Agent-Native Today's Software Serves Humans👨‍💻. Tomorrow's Users will be Agents🤖. CLI-Anything: Bridging the Gap Between AI Agents and the World's Software 🌐...
- 发布时间：2026-09-24 18:16 CST
- 链接：https://github.com/HKUDS/CLI-Anything

## Hacker News (AI stories)（hackernews-ai，en，本窗口共 120 条）

### 1. Anthropic resumes charging for requests blocked by safeguards
- 摘要：Today, we'll resume charging for requests our safeguards block before Claude responds. This only applies in categories with low false positive rates: biology, distillation attacks, and frontier LLM development. We've seen some coordinated attacks on our systems in recent weeks, and this is one laye…
- 作者：jeudesprits
- 发布时间：2026-09-25 02:42 CST
- 链接：https://twitter.com/ClaudeDevs/status/2103170368794185758

### 2. Creatine uptake enhances antitumor immunity
- 作者：lormayna
- 发布时间：2026-09-25 02:24 CST
- 链接：https://www.cell.com/iscience/fulltext/S2589-0042(26)00811-4

### 3. If you don't have the factories, you lose the expertise
- 摘要：Mainstream economists have been advocating for the marvellous effects of global trade for decades. Who needs these factory jobs anyway? We'll be designing the robots and the nuclear rockets. Except that, no. It does not work like that. If you have the factories, sooner or later, you get the designer...
- 作者：ibobev
- 发布时间：2026-09-25 01:52 CST
- 链接：https://lemire.me/blog/2026/09/24/if-you-dont-have-the-factories-you-lose-the-expertise/

## Product Hunt — AI（producthunt-ai，en，本窗口共 8 条）

### 1. Floot MCP
- 摘要：Build and ship web and mobile apps inside Claude or ChatGPT Discussion | Link
- 作者：Yuj Yao
- 发布时间：2026-09-24 04:54 CST
- 链接：https://www.producthunt.com/products/floot

### 2. Harness Manager
- 摘要：Your AI coding stack manager, all in one place Discussion | Link
- 作者：Sebastian Solano
- 发布时间：2026-09-24 02:17 CST
- 链接：https://www.producthunt.com/products/harness-manager

### 3. Subscrr
- 摘要：Build a financial plan and ask what to cancel Discussion | Link
- 作者：Artur Mineev
- 发布时间：2026-09-23 20:37 CST
- 链接：https://www.producthunt.com/products/subscrrr

## Reddit AI subreddits (hot)（reddit-ai-hot，en，本窗口共 7 条）

### 1. Is GPT-6-Sol just the newer version of GPT-5.6-Terra ?
- 摘要：I have been using GPT-6-Sol for the last few days after using 5.6-Sol for a while. It seems useless compared to 5.6. Is 6-Sol just the newer version of Terra? It has the same pricing as 5.6-Terra and it seems about on par with it. I have definitely had to switch back to 5.6 for now.
- 作者：Late_Change5029
- 发布时间：2026-09-24 19:50 CST
- 链接：https://www.reddit.com/r/OpenAI/comments/1woziaj/is_gpt6sol_just_the_newer_version_of_gpt56terra/

### 2. Prince Harry walks off stage awkwardly after teleprompter stops working during AI speech
- 摘要：The Duke of Sussex, Prince Harry, reportedly left the stage uncomfortably after the teleprompter stopped working during his AI speech.
- 作者：iceCupa
- 发布时间：2026-09-24 19:44 CST
- 链接：https://www.soapcentral.com/entertainment/prince-harry-walks-stage-awkwardly-teleprompter-stops-working-ai-speech

### 3. Japanese Animator Breaks Down How He Made an Anime MV Using Seedance
- 作者：PointmanW
- 发布时间：2026-09-24 19:24 CST
- 链接：https://v.redd.it/qk3b9qhhdgrh1

## Reddit AI subreddits (new)（reddit-ai-new，en，本窗口共 503 条）

### 1. FreedomIntelligence/HuatuoGPT-3-27B · Hugging Face
- 摘要：from FreedomIntelligence: HuatuoGPT-3-27B is a medical LLM built on Qwen3.8-27B with One-stage Policy Optimization (OnePO) . OnePO adapts language models to medicine in a single reinforcement-learning stage, without preceding domain-specific supervised fine-tuning. Teacher responses provide temporar...
- 作者：jacek2023
- 发布时间：2026-09-25 03:20 CST
- 链接：https://huggingface.co/FreedomIntelligence/HuatuoGPT-3-27B

### 2. Fall has arrived! Our GPUs are 100% efficient now.
- 作者：unchikuso
- 发布时间：2026-09-25 03:19 CST
- 链接：https://i.redd.it/2dw2je8qpirh1.jpeg

### 3. Claude Global Markets AI Mood - Update hourly and free to use
- 摘要：A concise, real‑time snapshot of market sentiment powered by AI, refreshed every hour to highlight shifts in optimism, fear, and momentum across global markets using Sonnet model 5. The AI Mood is on top stripe.
- 作者：Prestigious-Bank2145
- 发布时间：2026-09-25 03:17 CST
- 链接：https://gmdmarkets.com

## 智源社区（baai-hub，zh，本窗口共 20 条）

### 1. Nat. Rev. Drug Discov. | 药物靶点格局的演变
- 摘要：DRUG ONE 进入21世纪以来，遗传学、基因组学、蛋白质组学、结构生物学、自动化筛选和数据科学的快速发展，以及治疗形式从传统小分子向抗体、寡核苷酸和其他生物制剂扩展，显著改变了药物发现的靶点空间。研究人员系统梳理了过去25年的药物靶点变化。截至2025年6月，已获批药物共涉及686个作用机制靶点，由1,702种药物调控，其中79%为小分子药物、19%为生物制剂，其余为其他治疗形式。与20世纪主要集中于酶、G蛋白偶联受体（GPCR）和离子通道的传统格局相比，现代药物发现正在进入由新靶点、新治疗形式以及更高靶向精度共同驱动的阶段。 药物产生获批治疗作用所直接依赖的分子通常被称为作用机制（MoA...
- 作者：DrugAI
- 发布时间：2026-09-25 02:40 CST
- 链接：https://hub.baai.ac.cn/view/58250

### 2. Sci. Adv. | scProtoTransformer 实现生物学数据上的多尺度参考映射
- 摘要：如果把生命比作一本多层级的书——基因是字母，通路是词语，细胞是句子，而一个人，是整本书。过去十年，单细胞测序让我们第一次能“逐字”阅读这本生命之书，但如何把散布在数以亿计细胞里的信息，从分子、细胞一路拼到个体层面，始终缺少一套统一的方法。 近日，北京大学陈语谦团队联合香港城市大学（东莞）陈观兴团队、中山大学由林麟团队，在 Science Advances 发表题为“scProtoTransformer: Scalable reference mapping across molecules, cells, and donors”的研究论文。团队提出原型驱动的 Transformer 架构 sc...
- 作者：DrugAI
- 发布时间：2026-09-25 02:30 CST
- 链接：https://hub.baai.ac.cn/view/58249

### 3. 出海经营Agent“小元AI”入驻腾讯WorkBuddy：找买家、写开发信、谈生意一条龙
- 摘要：允中 发自 凹非寺 量子位 | 公众号 QbitAI AI办公赛道，率先进入“集团军作战”阶段。 8月末字节跳动正式发布“豆包工作”，将TRAE、扣子（Coze）整体并入豆包体系，并以飞书组织能力为底座；阿里巴巴已于8月初整合QoderWork、悟空、MuleRun三款智能体推出“千问办公”，全面瞄准钉钉生态的企业级市场；腾讯则通过整合QClaw团队，将WorkBuddy打造为国内用户规模领先的AI原生桌面办公智能体。 竞争焦点，已从“谁能答得更准”升级为“ 谁能把事办好 ”。 海外，前沿研究的重心同样指向“ 自主性与进化能力 ”。 Anthropic近期发布关于递归自我改进（RSI）的系统论...
- 作者：量子位
- 发布时间：2026-09-24 22:50 CST
- 链接：https://hub.baai.ac.cn/view/58248

---
共列出 154 条（窗口内采集总数 1772 条，来自 59 个信源）

## OpenClaw 推送提示
请基于本文件生成中文 Daily AI News 推送，不要联网，不要抓原文，不要扩展搜索。
优先 Tier 1 一手来源和国内外媒体中被多个信源同时报道的事件；Tier 3 社交条目只做补充。
每日只保留最新内容，覆盖更新。
