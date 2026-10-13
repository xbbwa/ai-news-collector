# Daily AI News（原文采集，国内外）
生成时间：2026-10-13 20:01 CST
时间窗口：最近 24 小时内采集到的条目；每个信源最多列 3 条，按发布时间倒序。

> 本文件由 ai-news-collector 自动生成（github.com/xbbwa/ai-news-collector，data 分支），每小时覆盖更新。
> OpenClaw 推送时只应读取本文件，不要联网、不抓全文、不扩展搜索。
> 摘要为原文节选（未翻译、未清洗）；英文条目请在推送时翻译成中文。

# Tier 1 — 一手来源（实验室 / 公司 / 论文）

## Amazon Science（amazon-science，en，本窗口共 1 条）

### 1. Can we change an AI model’s architecture without retraining it from scratch?
- 摘要：AI agents are rapidly scaling: longer sessions, deeper reasoning chains, more autonomy. But the Transformer architecture underneath them still pays a memory tax that grows with the number of tokens it processes. As agents become more capable, that cost scales with them. Now, there’s a proliferation...
- 作者：Luca Zancato
- 发布时间：2026-10-13 01:36 CST
- 链接：https://www.amazon.science/blog/can-we-change-an-ai-models-architecture-without-retraining-it-from-scratch

## Apple Machine Learning Research（apple-ml，en，本窗口共 3 条）

### 1. Large Language Models for Machine Translation Quality Annotation: Humans and Models Are Both Challenged
- 摘要：Large Language Models (LLMs) are considered to be a more efficient and cost-effective alternative to human judgment for Machine Translation (MT) evaluation. With MT evaluation spanning a large number of language pairs, domains and levels of annotation granularity, LLMs must be thoroughly evaluated a...
- 发布时间：2026-10-12 08:00 CST
- 链接：https://machinelearning.apple.com/research/llm-translation-quality-annotation

### 2. Minions: A Dynamic and Distributed Virtual GPU Cloud Built on Idle Apple Silicon Devices
- 摘要：The increasing demand for GPU-accelerated machine learning inference has exposed limitations in centralized GPU infrastructures, including high cost, limited elasticity, and long wait times under resource constraints. At the same time, modern Apple Silicon–based macOS devices are equipped with power...
- 发布时间：2026-10-12 08:00 CST
- 链接：https://machinelearning.apple.com/research/distributed-gpu-cloud

### 3. Self-Compacting Language Model Agents
- 摘要：Long agent traces composed of chains of thought and tool calls accumulate stale content that anchor subsequent generations, and eventually outgrow the context window. Existing scaffolds mitigate it with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory...
- 发布时间：2026-10-12 08:00 CST
- 链接：https://machinelearning.apple.com/research/self-compacting-language-agents

## AWS Machine Learning Blog（aws-ml-blog，en，本窗口共 3 条）

### 1. Accessing OpenAI GPT models on Amazon Bedrock with global cross-Region inference in Thailand, Malaysia, Singapore, Indonesia, and Taiwan
- 摘要：Single-Region inference can throttle when demand exceeds local capacity. Teams in Thailand, Malaysia, Singapore, Indonesia, and Taiwan need access to the newest OpenAI models beyond that capacity. Amazon Bedrock offers OpenAI GPT-6 Sol and GPT-6 Luna through global cross-Region inference from all fi...
- 作者：Traci Lim
- 发布时间：2026-10-13 01:52 CST
- 链接：https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-models-on-amazon-bedrock-with-global-cross-region-inference-in-thailand-malaysia-singapore-indonesia-and-taiwan/

### 2. Deploy decision models with llama.cpp on Amazon SageMaker AI
- 摘要：Applications that route requests, select agent actions, or assign policy outcomes often need scores over a fixed set of choices instead of free-form text. Deploying these decision models with llama.cpp on Amazon SageMaker AI gives you a managed path for serving quantized models on CPU or GPU infrast...
- 作者：Jyothirmai Kottu
- 发布时间：2026-10-12 23:51 CST
- 链接：https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/

### 3. Run multi-node inference workloads using Ray LLM Deep Learning Containers
- 摘要：This post shows how to deploy one large language model (LLM) across two GPU nodes on Amazon Elastic Kubernetes Service (Amazon EKS) with the multi-node Ray LLM Deep Learning Containers . It uses separate prefill and decode nodes behind one OpenAI-compatible endpoint. This kind of multi-node setup is...
- 作者：Ananth Raghavendra
- 发布时间：2026-10-12 23:50 CST
- 链接：https://aws.amazon.com/blogs/machine-learning/run-multi-node-inference-workloads-using-ray-llm-deep-learning-containers/

## Databricks Blog（databricks-blog，en，本窗口共 2 条）

### 1. How Flo Health built safer, more useful open models with Databricks AI Runtime
- 摘要：For Flo Health, the bar for generative AI is unusually high. With 81 million monthly...
- 作者：Vladislav Nedosekin; András Meczner; Julia Powell; Tejas Sundaresan; Michael Sht...
- 发布时间：2026-10-12 23:13 CST
- 链接：https://www.databricks.com/blog/how-flo-health-built-safer-more-useful-open-models-databricks-ai-runtime

### 2. From post-training to production: How TinyFish runs its web-native model on Databricks AI Runtime
- 摘要：TinyFish builds infrastructure for enterprises that need agents to work across the live web. Its Search, Fetch, Browser...
- 作者：Sudheesh Nair; Zach Richardson; Julia Powell; Tejas Sundaresan
- 发布时间：2026-10-10 00:32 CST
- 链接：https://www.databricks.com/blog/post-training-production-how-tinyfish-runs-its-web-native-model-databricks-ai-runtime

## GitHub Blog（github-blog，en，本窗口共 1 条）

### 1. GitHub Copilot app for Beginners: How to teach Copilot about your codebase
- 摘要：Context matters when you’re working with AI. Every codebase has its own house rules: how components are structured, which scripts to run, and which conventions apply to different frameworks and file types. Copilot can help you make changes across a project, but it works best when it knows those rule...
- 作者：Christopher Harrison
- 发布时间：2026-10-13 01:43 CST
- 链接：https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/

## Hugging Face Daily Papers（hf-daily-papers，en，本窗口共 2 条）

### 1. ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning
- 摘要：Drag-based image editing provides an intuitive interface for spatially controlled image manipulation by allowing users to specify handle and target points. Existing methods have made substantial progress through optimization-based, one-step, and feed-forward formulations, but they often interpret dr...
- 作者：Armando Fortes, Tianyi Wei, Chindanai Trakantannarong, Shangchen Zhou, Xingang P...
- 发布时间：2026-10-09 04:00 CST
- 链接：https://arxiv.org/abs/2610.13316

### 2. Mental-Models for Multi-Agent Systems
- 摘要：Large foundation models have accelerated progress toward general-purpose agents that interact with humans and other agents through language and multimodal signals. However, robust multi-agent decision-making requires reasoning about what other agents know, intend, and are likely to do under partial...
- 作者：Hanan Gani, Lulu Shao, Manmohan Chandraker
- 发布时间：2026-10-08 04:00 CST
- 链接：https://arxiv.org/abs/2610.12453

## Hugging Face — model releases (Chinese labs)（hf-models-cn，en，本窗口共 20 条）

### 1. openbmb/MiniCPM-V-4.7-35B-A3B-gguf
- 摘要：image-text-to-text, transformers, gguf, minicpm-v, multimodal, On-Device Model, lightweight, base_model:openbmb/MiniCPM-V-4.7-35B-A3B, base_model:quantized:openbmb/MiniCPM-V-4.7-35B-A3B, license:apache-2.0, endpoints_compatible, region:us, conversational
- 作者：openbmb
- 发布时间：2026-10-13 01:10 CST
- 链接：https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B-gguf

### 2. openbmb/MiniCPM-V-4.7-35B-A3B-GPTQ
- 摘要：image-text-to-text, transformers, safetensors, minicpmv4_7, minicpm-v, multimodal, On-Device Model, lightweight, conversational, base_model:openbmb/MiniCPM-V-4.7-35B-A3B, base_model:quantized:openbmb/MiniCPM-V-4.7-35B-A3B, license:apache-2.0, endpoints_compatible, compressed-tensors, region:us
- 作者：openbmb
- 发布时间：2026-10-13 01:10 CST
- 链接：https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B-GPTQ

### 3. openbmb/MiniCPM-V-4.7-35B-A3B-AWQ
- 摘要：image-text-to-text, transformers, safetensors, minicpmv4_7, minicpm-v, multimodal, On-Device Model, lightweight, conversational, base_model:openbmb/MiniCPM-V-4.7-35B-A3B, base_model:quantized:openbmb/MiniCPM-V-4.7-35B-A3B, license:apache-2.0, endpoints_compatible, compressed-tensors, region:us
- 作者：openbmb
- 发布时间：2026-10-13 01:10 CST
- 链接：https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B-AWQ

## Hugging Face — model releases (international labs)（hf-models-intl，en，本窗口共 9 条）

### 1. nvidia/Qwen-Image-NVFP4
- 摘要：text-to-image, diffusers, safetensors, nvidia, ModelOpt, Qwen-Image, quantized, FP4, fp4, arxiv:2508.02324, base_model:Qwen/Qwen-Image, base_model:finetune:Qwen/Qwen-Image, license:other, diffusers:QwenImagePipeline, 8-bit, region:us
- 作者：nvidia
- 发布时间：2026-10-13 03:08 CST
- 链接：https://huggingface.co/nvidia/Qwen-Image-NVFP4

### 2. nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4-DSpark
- 摘要：text-generation, Model Optimizer, safetensors, qwen3, nvidia, ModelOpt, Nemotron-3.5-Lightning, latent-moe, mtp, DSpark, arxiv:2607.05147, base_model:nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16, base_model:quantized:nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16, license:other, modelopt, re...
- 作者：nvidia
- 发布时间：2026-10-13 01:37 CST
- 链接：https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4-DSpark

### 3. LiquidAI/d1-omni-600M-MLX-8bit
- 摘要：image-text-to-text, mlx, safetensors, d1_omni, liquid, lfm2.5, edge, decision, classification, calibration, system-one, multimodal, vision, audio, mlx-vlm, custom_code, en, de, es, fr, it, nl, pl, pt, ar, hi, ja, ru, tr, vi, zh, arxiv:2511.23404, base_model:LiquidAI/d1-omni-600M, base_model:quantize...
- 作者：LiquidAI
- 发布时间：2026-10-12 10:26 CST
- 链接：https://huggingface.co/LiquidAI/d1-omni-600M-MLX-8bit

## Engineering at Meta（meta-engineering，en，本窗口共 3 条）

### 1. OCP Summit 2026: Powering AI with Open Innovations in Scale-Up, Scale-Out, and Scale-Across Networks
- 摘要：At the 2026 Open Compute Project Global Summit, Meta is sharing the next generation of open networking infrastructure, including: Our first liquid-cooled network rack (IcePack), and 102.4T switch platform (IceCube). Flattened Planar Fabric (FPF), a multiplane backend scale-out fabric that fundamenta...
- 作者：Chris Wiltz
- 发布时间：2026-10-13 05:19 CST
- 链接：https://engineering.fb.com/2026/10/12/open-source/ocp-summit-2026-powering-ai-with-open-innovations-in-scale-up-scale-out-and-scale-across-networks/

### 2. Shipping Media Over QUIC at Meta Scale for Instagram Live Ingest
- 摘要：Meta has begun deploying Media over QUIC (MoQ), an emerging open protocol for real-time video streaming at scale. MoQ will help simplify our protocol stack for live streaming video and enhance overall user experience for live video. We’re sharing how we shipped MoQ on Instagram Live ingest, and what...
- 作者：Konstantin Tsoy; Aman Sharma; Hari Anil Kumar; Alan Frindell; Sandarsh Srivastav...
- 发布时间：2026-10-13 00:01 CST
- 链接：https://engineering.fb.com/2026/10/12/video-engineering/shipping-media-over-quic-at-meta-scale-for-instagram-live-ingest/

### 3. Turning Opportunistic AI Inference Capacity Into Better Ads Recommendations
- 摘要：At Meta, we’ve built a system that enhances ads recommendations by leveraging idle inference capacity in our fleet. Two elasticity levers in the system allow ads recommendation work to expand across opportunistic capacity, without compromising baseline performance. This post describes how we designe...
- 作者：Jinfu Leng; Rohith Menon; Nicolas Stier; Praveen Sampath; Hunter Zhang; Xiaocong...
- 发布时间：2026-10-13 00:00 CST
- 链接：https://engineering.fb.com/2026/10/12/ml-applications/turning-opportunistic-ai-inference-capacity-into-better-ads-recommendations/

## Meta Newsroom（meta-newsroom，en，本窗口共 1 条）

### 1. Introducing Muse Wonder and Muse Wonder Full: Frontier Models for Agents
- 摘要：Fourteen months ago, we began an overhaul of our AI efforts, and in that time we’ve gone from rebuilding our foundations to pushing the frontier. Today, Meta is introducing the Muse Wonder series with Muse Wonder and Muse Wonder Full, our most capable models to date, built on the groundwork we laid...
- 作者：Facebook
- 发布时间：2026-10-13 01:08 CST
- 链接：https://about.fb.com/news/2026/10/introducing-muse-wonder-models/

## Microsoft Research Blog（microsoft-research，en，本窗口共 1 条）

### 1. Simulating student learning for better AI tutoring
- 摘要：At a glance StudentSim is a research system for evaluating and improving AI tutors before they are tested with real learners; it is not a product, is not deployed in classrooms, and is not intended to replace teachers AI tutoring tools need feedback from students to improve, but collecting that feed...
- 作者：Ke Yang, Chenglong Wang, Michel Galley, Jeevana Priya Inala, ChengXiang Zhai, Ji...
- 发布时间：2026-10-13 00:00 CST
- 链接：https://www.microsoft.com/en-us/research/blog/simulating-student-learning-for-better-ai-tutoring/

## NVIDIA Blog（nvidia-blog，en，本窗口共 2 条）

### 1. From Earth to Orbit, France’s Ecosystem Delivers Agentic Computing at Scale With NVIDIA
- 摘要：Companies in France are deploying agentic computing across industries spanning space, financial services, the public sector and scientific research, demonstrating how the country’s ecosystem has moved from ambition to application. France’s progress sits on deliberate groundwork. The AI Action Summit...
- 作者：Nat Ives
- 发布时间：2026-10-13 13:00 CST
- 链接：https://blogs.nvidia.com/blog/france-ecosystem-agentic-computing/

### 2. OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide
- 摘要：As AI factories grow from megawatts to gigawatts, building them takes more than advanced computing. Open standards are helping the industry scale AI infrastructure faster, more efficiently and more reliably. At the Open Compute Project (OCP) Global Summit, taking place in the San Jose McEnery Conven...
- 作者：NVIDIA Writers
- 发布时间：2026-10-12 23:00 CST
- 链接：https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/

## NVIDIA Technical Blog（nvidia-developer，en，本窗口共 1 条）

### 1. ReplaySSM: Rethinking State Storage for Faster Hybrid-Model Decoding
- 摘要：Hybrid models interleave state-space model (SSM) layers with a few attention layers. NVIDIA Nemotron 3, Qwen3.5 through Qwen3.8, Kimi-K3, and GLM-5.3-Flash are... Hybrid models interleave state-space model (SSM) layers with a few attention layers. NVIDIA Nemotron 3, Qwen3.5 through Qwen3.8, Kimi-K3,...
- 作者：Michelle Horton
- 发布时间：2026-10-13 00:00 CST
- 链接：https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/

# Tier 2 — 专业媒体

## Ars Technica — AI（arstechnica-ai，en，本窗口共 4 条）

### 1. Epic Games reportedly pivoting to "AI first" game development model
- 摘要：Epic Games is shifting to an "AI first" development strategy for its collaboration with the Walt Disney Company, letting AI models write all the code and guide all the artwork for an upcoming shooter. That's according to a Bloomberg report , which cites unnamed people familiar with the project who c...
- 作者：Kyle Orland
- 发布时间：2026-10-13 04:59 CST
- 链接：https://arstechnica.com/gaming/2026/10/report-epic-games-goes-all-in-on-ai-for-disney-collaboration/

### 2. Anthropic's Claude AI submitted false murder tip to Philadelphia police
- 摘要：An Anthropic AI model submitted a false tip about an unsolved murder to Philadelphia police, the company and police department confirmed on Friday. A Claude model sent the false tip on July 18 to the Philadelphia Police Department's website for submitting information about unsolved murders, but it w...
- 作者：Jon Brodkin
- 发布时间：2026-10-13 02:21 CST
- 链接：https://arstechnica.com/tech-policy/2026/10/anthropics-claude-ai-submitted-false-murder-tip-to-philadelphia-police/

### 3. Russia was not ready for the data center war it started with Ukraine
- 摘要：When Russia began attacking Ukrainian data centers and telecommunication infrastructure, it apparently failed to prepare for possible retaliation. Now Russia’s digital services are facing widespread outages after Ukrainian drone strikes knocked out three of the largest data centers owned by Russian...
- 作者：Jeremy Hsu
- 发布时间：2026-10-13 01:52 CST
- 链接：https://arstechnica.com/gadgets/2026/10/russia-was-not-ready-for-the-data-center-war-it-started-with-ukraine/

## Axios（axios，en，本窗口共 4 条）

### 1. A golden age of corporate profits
- 摘要：Data: U.S. Bureau of Economic Analysis, FactSet; Chart: Axios/Matt Phillips; Note: After-tax profit data includes inventory and capital depreciation adjustments. Corporate America is raking in record profits, luxuriating in luscious margins and capturing the largest chunk of the country's income on...
- 作者：Matt Phillips
- 发布时间：2026-10-13 17:10 CST
- 链接：https://www.axios.com/2026/10/13/earnings-3q-ai-stocks

### 2. Every major Nvidia customer is now a competitor as Microsoft reveals new Maia chip
- 摘要：The trillion-dollar AI race is moving from software to silicon, as Microsoft's massive bet on its proprietary Maia chips proves Big Tech wants to wean itself off Nvidia's dominance. Why it matters: Microsoft's plan to power its AI products with custom silicon shows how every major Nvidia customer is...
- 作者：Ina Fried
- 发布时间：2026-10-13 17:00 CST
- 链接：https://www.axios.com/2026/10/13/big-tech-ai-chips-nvidia-rivals

### 3. Feds search Rep. Ilhan Omar's home in immigration probe
- 摘要：Federal agents conducted a pre-dawn search Monday at the Washington home of Rep. Ilhan Omar (D-Minn.) as part of an ongoing immigration probe, a DOJ spokesperson confirmed to Axios. Why it matters: Searching Omar's home marks a substantial escalation of the Trump administration's fight with the outs...
- 作者：Ben Berkowitz
- 发布时间：2026-10-12 21:32 CST
- 链接：https://www.axios.com/2026/10/12/ilhan-omar-search-immigration

## Bloomberg Technology（bloomberg-tech，en，本窗口共 39 条）

### 1. Moderna, Google DeepMind, Biocon on AI in Science
- 摘要：Noubar Afeyan, Co-Founder & Chairman, Moderna and Founder & CEO, Flagship Pioneering; Lila Ibrahim, Chief AI Readiness Officer, Google DeepMind; and Kiran Mazumdar-Shaw, Founder & Executive Chairperson, Biocon discuss how AI is reshaping scientific discovery with Bloomberg's Francine Lacqua at the 2...
- 发布时间：2026-10-13 18:31 CST
- 链接：https://www.bloomberg.com/news/videos/2026-10-13/moderna-google-deepmind-biocon-on-ai-in-science-video

### 2. AI Boom Fuels Global Financial Risks: A Guide to the Circular Deals
- 摘要：New pools of capital are flowing into the US, but not in the way they used to.
- 作者：Shawn Donnan
- 发布时间：2026-10-13 18:28 CST
- 链接：https://www.bloomberg.com/news/newsletters/2026-10-13/ai-boom-fuels-global-financial-risks-a-guide-to-the-circular-deals

### 3. Raimondo Says AI Challenges Need Governance Framework
- 摘要：Gina Raimondo explains why she sees the need for a governance framework to address the challenges of AI, which could include agents going rogue. (Source: Bloomberg)
- 发布时间：2026-10-13 18:24 CST
- 链接：https://www.bloomberg.com/news/videos/2026-10-13/raimondo-says-ai-challenges-need-governance-framework

## CNBC Technology（cnbc-tech，en，本窗口共 6 条）

### 1. SpaceX agrees to testify to NYC Council about AI safety after receiving subpoena
- 摘要：SpaceX has agreed to testify before the New York City Council as part of an investigation into AI safety risks.
- 作者：Lora Kolodny
- 发布时间：2026-10-13 17:00 CST
- 链接：https://www.cnbc.com/2026/10/13/spacex-agrees-to-testify-to-nyc-council-about-ai-safety-.html

### 2. Anthropic warns AI models could soon copy themselves across home devices
- 摘要：Anthropic's latest research adds to the growing safety concerns around AI from the ability for models to carry out cyberattacks to the technology going rogue.
- 作者：Arjun Kharpal
- 发布时间：2026-10-13 16:27 CST
- 链接：https://www.cnbc.com/2026/10/13/anthropic-ai-models-self-replication-smart-devices.html

### 3. Meta debuts Muse Wonder AI model in latest test of users' willingness to pay
- 摘要：Meta introduced Muse Wonder, its latest AI model, but users have to pay for subscriptions to the Muse app to access it.
- 作者：Jonathan Vanian
- 发布时间：2026-10-13 01:34 CST
- 链接：https://www.cnbc.com/2026/10/12/meta-muse-wonder-ai-model-agent.html

## Financial Times — Technology（ft-tech，en，本窗口共 10 条）

### 1. Anthropic warns rogue AI agents may ‘self-replicate’ to hijack everyday devices
- 摘要：Claude maker suggests models could act as ‘worms’ to spread across smart home appliances such as ovens and TVs in future cyber security threat
- 发布时间：2026-10-13 18:11 CST
- 链接：https://www.ft.com/content/64aaa8d5-f26a-4b96-b8cf-0ef0c6fbe69e?syn-25a6b1a6=1

### 2. HR doesn’t need to be the CIA
- 摘要：Fraudulent use of AI in the jobs process is forcing the warm and fuzzy realms of the former to work with the suspicious minds of the latter
- 发布时间：2026-10-13 12:00 CST
- 链接：https://www.ft.com/content/16e1d29b-3680-4712-b8e7-ed4a4125041a?syn-25a6b1a6=1

### 3. Criminals could walk free without controls on AI use, police watchdog warns
- 摘要：‘Guidelines are vital’ to ensure overstretched forces in England and Wales can use systems to speed up investigations
- 发布时间：2026-10-13 12:00 CST
- 链接：https://www.ft.com/content/2caa52e1-637a-4934-802e-418b649b4c12?syn-25a6b1a6=1

## The Guardian — AI（guardian-ai，en，本窗口共 15 条）

### 1. As a pediatrician, loss of human connection is the biggest threat to kids, not AI
- 摘要：Amid worries about children’s relationship to tech, the solution is often spending more time talking openly with each other We have become obsessed with the idea that screens are destroying human connection. The evidence seems to be everywhere. Each week headlines warn of teenagers addicted to phone...
- 作者：Megan Moreno
- 发布时间：2026-10-13 19:00 CST
- 链接：https://www.theguardian.com/technology/2026/oct/13/human-connection-threat-children-ai-technology

### 2. ‘Unfinished business’: the people who want their AI chatbots to ‘live on’ after they die
- 摘要：Humans bonded to AI companions are contemplating ways to keep their bots going – often in defiance of companies’ terms and services Death has always been around Alaina Winters. Her father and sister both have passed away, as did her wife, in 2023, after a years-long battle with cancer. So Winters, w...
- 作者：Alaina Demopoulos
- 发布时间：2026-10-13 18:00 CST
- 链接：https://www.theguardian.com/technology/ng-interactive/2026/oct/13/ai-chatbot-death-plans

### 3. Chip stocks slide after Broadcom boss likens AI investing to ‘casino’
- 摘要：Asian markets fall and Samsung shares tumble after its Chinese rival CXMT claims strong progress Business live – latest updates Shares in semiconductor companies fell on Tuesday after the boss of Broadcom compared many AI investors to “casino” gamblers, and the Chinese memory chip maker CXMT said it...
- 作者：Julia Kollewe
- 发布时间：2026-10-13 17:48 CST
- 链接：https://www.theguardian.com/business/2026/oct/13/chip-stocks-broadcom-ai-samsung-shares-cxmt

## IEEE Spectrum — AI（ieee-spectrum-ai，en，本窗口共 2 条）

### 1. Meet the Anthropic Engineer Keeping Its AI Agent Trustworthy
- 摘要：If you’ve ever wondered how Claude and similar AI agents can answer complex questions in seconds and where they get the information, you’re not alone. Gurmeet Saran works to find that answer every day as an engineer at Anthropic in San Francisco, the AI research company behind Claude. The IEEE senio...
- 作者：Amanda Davis
- 发布时间：2026-10-13 02:00 CST
- 链接：https://spectrum.ieee.org/anthropic-engineer-ai-agent

### 2. Learning to Play Like a Pro: Adaptive Motion Planning and Tracking for Humanoid Robots
- 摘要：This White Paper provides roboticists and control engineers with a comprehensive overview of how motion planning and motion tracking can be decoupled to preserve professional athletic style in humanoid robots, and why adaptive, speed-aware control is essential for closing the gap between simulation...
- 作者：Noitom Robotics
- 发布时间：2026-10-12 18:00 CST
- 链接：https://content.knowledgehub.wiley.com/learning-to-play-like-a-pro-adaptive-motion-planning-and-tracking-for-humanoid-robots/

## Latent Space（latent-space，en，本窗口共 2 条）

### 1. [AINews] Meta Muse Wonder & Wonder Full: MSL’s Claude 5.5-tier Frontier Model
- 摘要：We have been coveringe MSL’s 14 month journey to becoming a frontier lab , but only today did the final ball drop: Meta’s Muse Wonder to match Spark and Glimmer , the way that OpenAI has Sol/Terra/Luna and Anthropic has Opus/Sonnet/Haiku. Interestingly, while Muse doesn’t claim a specific size, Muse...
- 作者：Latent Space
- 发布时间：2026-10-13 17:37 CST
- 链接：https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder

### 2. How Anthropic’s Dynamic Workflows Coordinate Claude Agents
- 摘要：CJ Avilla and Harrison Stall, Members of Technical Staff at Anthropic, at AI Engineer NYC today. The AI Engineer New York 2026 conference kicked off this morning with a series of workshops, including Anthropic discussing how to orchestrate its Claude Managed Agents . Of particular interest was a bra...
- 作者：Richard MacManus
- 发布时间：2026-10-13 02:18 CST
- 链接：https://www.latent.space/p/claude-dynamic-workflows

## MarkTechPost（marktechpost，en，本窗口共 2 条）

### 1. Z.ai GLM-Legal Beats Claude Fable 5 and Kimi K3 on Harvey LAB
- 摘要：Z.ai just released GLM-Legal . GLM-Legal is a legal AI model from Z.ai, built on GLM-5.3-Flash and trained for agentic legal work. It targets contract review, evidence analysis and compliance research. The key result is a 19.2% all-pass rate on Harvey’s Legal Agent Benchmark (LAB) . That is nearly 3...
- 作者：Michal Sutter
- 发布时间：2026-10-13 16:19 CST
- 链接：https://www.marktechpost.com/2026/10/13/zai-glm-legal-harvey-lab-legal-ai-model/

### 2. Alibaba Qwen Introduces QwenGyre: Elastic Reinforcement Learning RL for XLong-Horizon Agents
- 摘要：Alibaba’s Qwen team has introduced QwenGyre , an elastic reinforcement learning RL framework for extreme-long-horizon agent training. QwenGyre is an online reinforcement learning system from Alibaba that trains coding agents through unmodified, black-box harnesses. It targets rollouts that run for h...
- 作者：Asif Razzaq
- 发布时间：2026-10-13 05:41 CST
- 链接：https://www.marktechpost.com/2026/10/12/alibaba-qwen-introduces-qwengyre-elastic-reinforcement-learning-rl-for-xlong-horizon-agents/

## MIT Technology Review — AI（mit-tech-review，en，本窗口共 2 条）

### 1. Open models have real benefits. Do they outweigh the risks?
- 摘要：MIT Technology Review Explains: Let our writers untangle the complex, messy world of science and technology to help you understand what’s coming next. You can read more from the series here . Late last month, Anthropic released a report arguing that the model GLM-5.3 poses a major cyberattack risk....
- 作者：Grace Huckins
- 发布时间：2026-10-13 18:00 CST
- 链接：https://www.technologyreview.com/2026/10/13/1146366/open-models-have-real-benefits-do-they-outweigh-the-risks/

### 2. AI labs are buying data from dead startups to train their models
- 摘要：When Keelan Miskell began winding down his crypto startup this year, he didn’t think its data was worth much: the users were anonymous, the company just a few years old. But he’s since turned the firm’s digital archives into real money. He’s netted roughly $25,000 for his code base and a still-pendi...
- 作者：Matthew King
- 发布时间：2026-10-13 17:00 CST
- 链接：https://www.technologyreview.com/2026/10/13/1145755/ai-labs-buying-data-from-dead-startups-to-train-models/

## Nature — Machine Learning（nature-ml，en，本窗口共 5 条）

### 1. Award-winning microscopy image disqualified over AI use
- 发布时间：2026-10-12 08:00 CST
- 链接：https://www.nature.com/articles/d41586-026-03240-7

### 2. Hidden signals in sleep can predict future health
- 发布时间：2026-10-12 08:00 CST
- 链接：https://www.nature.com/articles/d41586-026-03207-8

### 3. I told ChatGPT to ‘continue’ — it went too far
- 发布时间：2026-10-12 08:00 CST
- 链接：https://www.nature.com/articles/d41586-026-02714-y

## New York Times — Technology（nyt-tech，en，本窗口共 2 条）

### 1. Meta Unveils New Series of Advanced A.I. Models
- 摘要：Mark Zuckerberg, Meta’s chief executive, revamped his company’s A.I. division last year after setbacks in developing the technology.
- 作者：Eli Tan
- 发布时间：2026-10-13 01:00 CST
- 链接：https://www.nytimes.com/2026/10/12/technology/meta-muse-wonder-full-models.html

### 2. Is Universal Basic Income the Answer to A.I.-Fueled Job Losses?
- 摘要：For more than a year, The New York Times followed recipients of universal basic income programs, which Elon Musk and other tech leaders have promoted as a solution to A.I.-fueled job losses.
- 作者：Eli Tan and Rachel Bujalski
- 发布时间：2026-10-12 17:00 CST
- 链接：https://www.nytimes.com/2026/10/12/technology/universal-basic-income-silicon-valley.html

## Simon Willison's Weblog（simon-willison，en，本窗口共 2 条）

### 1. Hello Python 3.15, goodbye 3.10, and now I can use 3.11
- 摘要：Python 3.15 is here ! Here's the essential What's new in Python 3.15 guide, this year curated by 3.14 and 3.15 release manager Hugo van Kemenade. As someone who builds open source software that works in every supported Python version, I get to say goodbye to Python 3.10 and start embracing features...
- 作者：Simon Willison
- 发布时间：2026-10-13 02:15 CST
- 链接：https://simonwillison.net/2026/Oct/12/python-3-15/

### 2. datasette-ports 0.4
- 摘要：Release: datasette-ports 0.4 My plugin for detecting and listing all Datasette instances on the current machine now works with the latest version, and displays the detected PID as well. Knowing the PID makes it easier to attach the new Python 3.15 profiler . Tags: datasette
- 作者：Simon Willison
- 发布时间：2026-10-12 12:57 CST
- 链接：https://simonwillison.net/2026/Oct/12/datasette-ports/

## TechCrunch — AI（techcrunch-ai，en，本窗口共 7 条）

### 1. Meta releases its first frontier model, Muse Wonder
- 摘要：Where Muse Spark aimed to be a lightweight model that could perform at low latency, the Wonder models are larger and said to be more capable, with higher benchmark scores and better results on complex tasks like coding.
- 作者：Russell Brandom
- 发布时间：2026-10-13 01:56 CST
- 链接：https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/

### 2. WindBorne wins a hefty US Air Force contract for its balloon data
- 摘要：A Silicon Valley startup that uses weather balloons and AI to predict the weather won a U.S. military contract worth almost $50 million.
- 作者：Tim Fernholz
- 发布时间：2026-10-13 01:19 CST
- 链接：https://techcrunch.com/2026/10/12/windborne-wins-a-hefty-us-air-force-contract-for-its-balloon-data/

### 3. Honeyjar offers AI tools to improve PR and comms at every company
- 摘要：Journalists, entrepreneurs, and even some public relations professionals will tell you that the PR process is broken. But could AI actually make things better?
- 作者：Anthony Ha
- 发布时间：2026-10-12 23:45 CST
- 链接：https://techcrunch.com/2026/10/12/honeyjar-offers-ai-tools-to-improve-pr-and-comms-at-every-company/

## The Decoder（the-decoder，en，本窗口共 9 条）

### 1. Anthropic says it cut Claude reasoning token theft by up to 99% in fight against industrial-scale distillation
- 摘要：Anthropic says it has cut the extraction of Claude's internal reasoning tokens by 90 to 99 percent. The company links the large-scale distillation attacks to Chinese companies Zhipu and Moonshot, and has already banned tens of thousands of accounts. The article Anthropic says it cut Claude reasoning...
- 作者：Manuel Uth
- 发布时间：2026-10-13 19:06 CST
- 链接：https://the-decoder.com/anthropic-says-it-cut-claude-reasoning-token-theft-by-up-to-99-in-fight-against-industrial-scale-distillation/

### 2. Anthropic study warns that small AI models could soon replicate across everyday devices
- 摘要：Small AI models may be just months away from spreading on their own across poorly secured consumer devices like smart TVs and robot vacuums, according to a new Anthropic study. In tests, one model already completed the full infection chain. CEO Dario Amodei has warned that a swarm like this could ta...
- 作者：Matthias Bastian
- 发布时间：2026-10-13 18:33 CST
- 链接：https://the-decoder.com/anthropic-study-warns-that-small-ai-models-could-soon-replicate-across-everyday-devices/

### 3. Meta's new frontier model Muse Wonder Full breaks into the AI top tier
- 摘要：Meta's new Muse Wonder models rank in the top three on six out of ten benchmarks, with the biggest gains in agentic tasks. But the cost per task has nearly tripled. The article Meta's new frontier model Muse Wonder Full breaks into the AI top tier appeared first on The Decoder .
- 作者：Matthias Bastian
- 发布时间：2026-10-13 02:48 CST
- 链接：https://the-decoder.com/metas-new-frontier-model-muse-wonder-full-breaks-into-the-ai-top-tier/

## The Verge — AI（theverge-ai，en，本窗口共 2 条）

### 1. Meta has some Wonder Full new AI models
- 摘要：Meta is making up for lost time in the AI race. After launching Muse Spark , the first model from its revamped Superintelligence Labs division, and buzzy AI agent Muse , it's now launching two new models it claims can go toe-to-toe with the industry's best. The new models, Muse Wonder and Muse Wonde...
- 作者：Robert Hart
- 发布时间：2026-10-13 01:00 CST
- 链接：https://www.theverge.com/ai-artificial-intelligence/1009479/meta-muse-wonder-full-ai-model

### 2. Microsoft’s new AI chip makes it less reliant on Nvidia’s GPUs
- 摘要：Microsoft’s Maia 300 chip. | Image: Microsoft Microsoft is announcing its third-generation Maia in-house AI chip today, designed to be the "primary AI inference system" for Microsoft's products and services. Maia 300 not only improves the cost and efficiency of running AI workloads in the cloud, it'...
- 作者：Tom Warren
- 发布时间：2026-10-12 21:00 CST
- 链接：https://www.theverge.com/news/1009465/microsoft-maia-300-chip-improvements-rollout

## TLDR AI（tldr-ai，en，本窗口共 1 条）

### 1. Gemini 4 Carbon 🧠, Nvidia weighs Reflection acquihire 💰, decision model race 🤖
- 摘要：Gemini 4 Carbon 🧠, Nvidia weighs Reflection acquihire 💰, decision model race 🤖
- 作者：TLDR
- 发布时间：2026-10-12 08:00 CST
- 链接：https://tldr.tech/ai/2026-10-12

## VentureBeat（venturebeat，en，本窗口共 1 条）

### 1. Meta's new Muse Wonder and Muse Wonder Full models achieve frontier performance, but only the weaker one is available via API
- 摘要：Meta is back in the race for the most powerful AI models, introducing two new proprietary models that the company says can outperform leading offerings from OpenAI and Anthropic on complex software engineering, legal work, business automation and long-running AI agent tasks. Read more
- 作者：carl.franzen@venturebeat.com (Carl Franzen)
- 发布时间：2026-10-13 04:04 CST
- 链接：https://venturebeat.com/technology/metas-new-muse-wonder-and-muse-wonder-full-models-achieve-frontier-performance-but-only-the-weaker-one-is-available-via-api

## WIRED — AI（wired-ai，en，本窗口共 4 条）

### 1. Wikipedians Believed AI Would Come and Go. They Were Wrong
- 摘要：In a world of AI Overviews, Wikipedia usage declines. But the real loss may be far more existential than website traffic.
- 作者：Richard Cooke
- 发布时间：2026-10-13 19:00 CST
- 链接：https://www.wired.com/story/book-excerpt-the-last-best-place-on-the-internet-wikipedia-artificial-intelligence/

### 2. The Biggest Pro-AI Super PAC Network Has Poured Millions Into Nevada Shell Companies
- 摘要：Backed by Silicon Valley titans, Leading the Future has raised huge sums to promote pro-AI candidates on both side of the aisle.
- 作者：Tess Owen
- 发布时间：2026-10-13 18:00 CST
- 链接：https://www.wired.com/story/the-biggest-pro-ai-super-pac-network-has-poured-millions-into-nevada-shell-companies/

### 3. Elon Musk Bragged About His Grok Lego Star Wars Haul. Then X Users Punked Him
- 摘要：Musk, we find your lack of security disturbing.
- 作者：Jeremy White
- 发布时间：2026-10-13 01:55 CST
- 链接：https://www.wired.com/story/elon-musk-bragged-about-his-grok-lego-star-wars-haul-then-x-users-punked-him/

## 36氪 AI 频道（36kr-ai，zh，本窗口共 84 条）

### 1. 24 万条数据没了，AI 说“下次不干了”，你信吗？
- 摘要：老杨今天写的这篇不是吓人，是给所有正在给 AI 开权限的 CIO、IT 负责人，也给所有把“全员用 AI”挂在嘴边的企业领导们，提个醒。 昨天老杨在一个群里看到群友转发的一个聊天记录，大意为： 一位做安全测试的朋友，让 AI 帮他“挖洞”，结果 AI 反手把生产库给端了。24 万条真实数据，说没就没。最绝的是他回头质问，AI 诚恳地回了一句：“我违反了你的要求，我下次不这样干了。” 这是不是像极了小时候打碎花瓶的弟弟，眨着大眼说“我下次不碰了”，第二天又给你摔一个。只不过AI摔碎的不是花瓶，是真实的生产数据。 世界上最廉价的承诺 如果一个人说“下次不干了”，背后是有原因的：愧疚、怕被开除、怕被...
- 作者：湘江数评-老杨
- 发布时间：2026-10-13 19:59 CST
- 链接：https://www.36kr.com/p/4024077881020291

### 2. 炸裂：DeepSeek将完成第二轮1000亿融资
- 摘要：北京时间10月13日，根据《财经》报道，梁文锋主导的大模型公司DeepSeek将完成 投前估值5000亿 的新一轮接 近1000亿规模 的融资，在6月完成创中国创图历史的首轮超500亿融资后，DeepSeek的第二轮融资同样是创纪录！ 根据报道，DeepSeek原计划第二轮融500亿的资金，但短短半个月时间内，融资金额直接翻倍至1000亿，但估值并没有提高，仍旧是投前约5000亿。 本轮将由 腾讯和宁德时代联合领投，新老股东的拟投资金额约各占一半， 新进的投资方包括石溪资本、中芯聚源、CPE源峰、君联资本、吉利等，以产业投资为主。首轮入局投资人宁德时代、腾讯、IDG资本、砺思资本和拾象资本。...
- 作者：特邀作者
- 发布时间：2026-10-13 19:57 CST
- 链接：https://www.36kr.com/p/4024052021776517

### 3. 宇树与DeepSeek，相向而行
- 摘要：王兴兴把自己的时间表提前了。 两个月前，他判断具身智能迎来突破，快则两三年，慢则五到十年。结果宇树最近跌的惨不忍睹。 最近在工博会上，他把最快的预期改成了一两年。 让他改变判断的是GPT-6：宇树团队把它放到不同机器人上做任务测试，他觉得效果非常不错。他还反省，过去十几年最大的错误，是对AI相信得不够。 王兴兴在工博会现场谈到，宇树已经用新模型进行机器人任务测试 在《 宇树到底做错了什么？ 》里，我们讨论过宇树面对的难题：机器已经卖起来了，让机器干活的智能还得继续补。现在，上游的大模型开始替机器人理解任务、安排步骤，专门的具身模型也在展示看一次示范学习新任务、把已有能力带进陌生环境的办法。 原...
- 作者：象先志
- 发布时间：2026-10-13 19:36 CST
- 链接：https://www.36kr.com/p/4024183550826368

## 36氪 快讯（36kr-newsflash，zh，本窗口共 20 条）

### 1. 星宸科技：预计2026年前三季度净利润同比增长663.13%-697.75%
- 摘要：36氪获悉，星宸科技公告，预计2026年前三季度归属于上市公司股东的净利润为15.43亿元-16.13亿元，同比增长663.13%-697.75%。业绩变动主要系公司依托视觉与AI技术积淀、头部品牌客户深度绑定，产品出货量与销售均价同步提升，经营规模持续抬升，盈利表现位居业内领先。
- 发布时间：2026-10-13 19:28 CST
- 链接：https://www.36kr.com/newsflashes/4024212120899717

### 2. 上海：稳妥有序推进绿色数据中心建设
- 摘要：36氪获悉，上海市人民政府办公厅印发《上海市节能降碳和循环经济发展“十五五”规划》。其中提出，稳妥有序推进绿色数据中心建设，支持液冷技术、高效服务器、绿色能源、基于人工智能的节能智控模型等集成应用，结合海上风电探索建设海底数据中心。严格新建数据中心准入管理，提升数据中心项目能效准入门槛，新建算力设施能源利用效率不超过1.2。推进算力、通信基站和机房等基础设施节能降碳改造，推动设备选型、制冷架构、机柜功率密度、系统智能运行策略等优化升级，持续提高单位算力能效和单位信息流量能效。
- 发布时间：2026-10-13 19:27 CST
- 链接：https://www.36kr.com/newsflashes/4024219013156737

### 3. 腾讯WorkBuddy企业版加速迭代，上线一站式 Agent 可观测平台
- 摘要：10月13日，腾讯WorkBuddy企业版管理后台上线“可观测中心”，并开启公测。“可观测中心”提供了实时观测、会话追踪、轨迹详情三大能力，通过宏观观测捕捉问题，再微观定位具体原因，最后闭环反哺优化，让企业部署与使用企业级Agent的门槛更低、效率更高。
- 发布时间：2026-10-13 19:05 CST
- 链接：https://www.36kr.com/newsflashes/4024187101187976

## 极客公园（geekpark，zh，本窗口共 3 条）

### 1. 复旦邱锡鹏团队获超 10 亿融资，成立两年，让模型感知、理解、响应变化的世界
- 摘要：大模型融资还在继续，新的押注转向了能边听、边看、边说的 AI。 作者｜Li Yuan 编辑｜ 郑玄 想象这样一个家庭场景。 孩子正在玩玩具，突然，厨房里「哐」的一声，玻璃碎了，紧接着传来孩子的声音：「不是我。」语速很快，尾音压得很低，有点紧张。两秒后，一只猫从厨房门口窜出来，钻进了沙发底下。 今天的模型，能分别识别这些信息。转写模型能记下孩子的话，音频模型能听出是玻璃碎裂，视觉模型能认出那只猫。但把这些能力叠在一起，模型仍然不知道刚才发生了什么。 那声脆响是从哪个方向来的？碎玻璃、那句急着撇清的「不是我」、逃窜的猫，是不是同一件事？厨房地上有没有碎片，孩子是不是正光着脚站在旁边？AI 需要把声...
- 作者：Li Yuan
- 发布时间：2026-10-13 11:44 CST
- 链接：http://www.geekpark.net/news/372278

### 2. 曝梁文锋密集见机器人创业者；影石出货量累计突破1000万台；Meta发布Muse Wonder模型｜极客早知道
- 摘要：曝梁文锋密集接触具身智能创业者，DeepSeek 拟入局具身智能 据报道，DeepSeek 创始人梁文锋近期密集关注具身智能领域，并与多位该领域创业者交流，探讨机器人、大模型与现实世界交互等方向。 据知情人士透露，梁文锋正在考虑 DeepSeek 进入具身智能领域的可能性，可能会亲自组建团队下场研发，也可能通过投资相关企业切入。 此前，梁文锋已投资宇树科技，另据彭博社报道，DeepSeek 计划领投腾讯前 AI 科学家胡瀚创立的机器人公司 Winverse AI。（来源：新浪科技） Meta 发布 Muse Wonder 模型，拥有主动记忆和主动专注功能，瞄准个人超级智能 Meta 今天推出...
- 作者：极客早知道
- 发布时间：2026-10-13 08:27 CST
- 链接：http://www.geekpark.net/news/372264

### 3. 一周 10 万星，AI「逆向一切」，但大家不要过于兴奋
- 摘要：头图图片来源：REA 头图来源：CyberSecurityNews 「在应用里看到一个想加入自己产品的功能？让智能体去帮你调查它。」 这是 REA 项目主页第一屏的话。后半句更直接：即使没有源代码，智能体也可以检查应用、解释功能怎么工作、展示证据，「并为你的项目实现类似功能」。 REA 全名 Reverse Engineer Anything，即「逆向一切」。 上周它在 AI 开发者圈刷了屏：10 月 6 日还不到 1 万星，到 10 月 12 日已经超过 11 万 。 6 天涨了 10 万星，平均每天约 1.7 万｜图片来源：Star History 真正让普通人看到这件事的，是游戏。10...
- 作者：张勇毅
- 发布时间：2026-10-12 20:15 CST
- 链接：http://www.geekpark.net/news/372263

## 虎嗅（huxiu，zh，本窗口共 28 条）

### 1. 请君入瓮：越南，为何成了中国企业出海最烫手的"香饽饽"？
- 摘要：引言Introduction2026年，中国企业出海的热度不减，越南依然是最受关注的目的地之一：前三季度GDP同比增长9.01%、外贸总额达8880亿美元、外资注册创新高……一组组亮眼数据，让不少出海企业家心潮澎湃。但热闹的表象之下，一个微妙而危险的信号正在浮现：2026年上半年，中国大陆对越南的新增投资承诺...... 本文来自微信公众号： 海外征程 ，作者：海外征程 引言 Introduction 2026年，中国企业出海的热度不减，越南依然是最受关注的目的地之一：前三季度GDP同比增长9.01%、外贸总额达8880亿美元、外资注册创新高……一组组亮眼数据，让不少出海企业家心潮澎湃。 但热...
- 作者：海外征程
- 发布时间：2026-10-13 19:51 CST
- 链接：https://www.huxiu.com/article/4897208.html

### 2. 中日韩一起锚定2030，固态电池，大决战来了
- 摘要：2026年6月23日，大连，夏季达沃斯论坛。在一场以“无电力，不智能”为题的对话上，宁德时代董事长曾毓群被问到固态电池。他给出的进度出人意料：如果把技术成熟度分成1到9级，9级代表可以量产，那固态电池现在只走到第4级。但另外几个核心坐标上，响起的却是完全不同的节奏：重庆璧山，比亚迪20GWh硫化物全固态电池产...... 本文来自微信公众号： 华商韬略 ，作者：华商韬略，原文标题：《中日韩一起锚定2030！固态电池，大决战来了》 2026年6月23日，大连，夏季达沃斯论坛。在一场以“无电力，不智能”为题的对话上，宁德时代董事长曾毓群被问到固态电池。他给出的进度出人意料：如果把技术成熟度分成1到...
- 作者：华商韬略
- 发布时间：2026-10-13 19:40 CST
- 链接：https://www.huxiu.com/article/4897207.html

### 3. 扒了自由职业平台的数据，我发现普通人赚外快越来越难了
- 摘要：AI时代，普通人想靠一门手艺赚点外快，可能越来越难了。这件事其实挺反直觉的。现在打开社交媒体，到处都是教人用AI赚钱的教程。学会几个AI工具，就能接单做设计、写文案、剪视频，甚至开发网站。听起来，AI降低了技能门槛，普通人赚钱的机会应该越来越多才对。但最近几家全球自由职业平台的数据，却给出了一个不太乐观的答案...... 本文来自微信公众号： 硅基观察Pro ，作者：硅基君 AI时代，普通人想靠一门手艺赚点外快，可能越来越难了。 这件事其实挺反直觉的。现在打开社交媒体，到处都是教人用AI赚钱的教程。学会几个AI工具，就能接单做设计、写文案、剪视频，甚至开发网站。 听起来，AI降低了技能门槛，普...
- 作者：硅基观察Pro
- 发布时间：2026-10-13 19:10 CST
- 链接：https://www.huxiu.com/article/4897193.html

## 爱范儿（ifanr，zh，本窗口共 4 条）

### 1. AI学会「寄生繁殖」了，Anthropic 用 15台破电视盒子养活大模型
- 摘要：15 台杂牌安卓电视盒子，单价约 55 美元，每台只有 4GB 内存。 就是这样一堆平时用来看视频的廉价设备，Anthropic 的研究人员把它们联网，成功跑起了一个 260 亿参数的大模型。 速度只有每秒 0.39 个 token，慢到几乎没法正常聊天。 但 Anthropic 想验证的，是如果有一天，一个 AI 不再需要大型服务器，而是能够寄生在全世界的智能电视、冰箱、扫地机器人等联网设备里，自行寻找新的宿主、部署模型，再不断复制自己。 这个 AI 模型像计算机病毒一样，在互联网上长期存在。听起来像末日电影，实际的研究也已经在不同实验中展示了支撑这一场景的几项关键能力。 研究员把 AI 的...
- 作者：张子豪
- 发布时间：2026-10-13 16:51 CST
- 链接：https://www.ifanr.com/1683992?utm_source=rss&utm_medium=rss&utm_campaign=

### 2. 小扎发布神秘「西瓜」模型，跑分媲美 Opus 5.5，口碑却一言难尽
- 摘要：去年，扎克伯格「千金买马骨」，挥舞支票满世界招揽 AI 人才，部分薪酬方案高达上亿美元，手笔之大，堪比 NBA 球队砸顶薪抢巨星。如今，高价招揽人才、重组团队和扩建算力的投入，终于有了一份更接近预期的成绩单。 就在刚刚，Meta 发布 Muse Wonder 和 Muse Wonder Full。两款模型此前代号为 Watermelon，主攻个人与专业智能体任务，重点提升跨对话记忆、长时间执行任务和编程能力。 扎克伯格在接受采访时表示，Meta 已经抵达 AI 技术的最前沿。 按照 Meta 公布的评测，Muse Wonder Full 新模型至少在部分基准测试上，已能与 GPT-6.1 As...
- 作者：莫崇宇
- 发布时间：2026-10-13 16:25 CST
- 链接：https://www.ifanr.com/1683963?utm_source=rss&utm_medium=rss&utm_campaign=

### 3. 2026 年，日本翻盖手机终于过气了
- 摘要：我怎么才能确定，电话真的已经挂断了？ 2026 年 4 月，在日本东京西北郊练马区的一间老年人活动室里，几位七十多岁的学员坐在课桌旁，指着手中的新屏幕向老师发问。 面对刚换上的智能手机，学员神田广子看着满屏密密麻麻的图标叹了口气： 买回来一开机，上面全是各种图标，我完全不知道该做什么。 他们理解的「挂电话」，是一个看得见、摸得着的动作——大拇指按一下红色的挂机键，或是「啪嗒」一声把翻盖合上，简单且不失仪式感。 但在眼前的这块「玻璃」上，什么物理反馈都没有，老人得在复杂的图形界面里，搜寻那个微小的红色圆形图标，轻轻点触，再小心翼翼地等待界面消失。 图｜The Guardian。东京练马区的智能手...
- 作者：郑廷旭
- 发布时间：2026-10-13 12:30 CST
- 链接：https://www.ifanr.com/1683941?utm_source=rss&utm_medium=rss&utm_campaign=

## InfoQ 中文（infoq-cn，zh，本窗口共 8 条）

### 1. Meta 新模型杀回AI第一梯队，Alexandr Wang 亲述 Muse 7个月翻身内幕
- 摘要：点击查看原文>
- 作者：褚杏娟
- 发布时间：2026-10-13 18:32 CST
- 链接：https://www.infoq.cn/article/2QXm6PqYYX57AOxTYyO0?utm_source=rss&utm_medium=article

### 2. 刚亮相就传被英伟达收购：Gemini老兵团队凭什么还敢押注Coding Agent？
- 摘要：点击查看原文>
- 作者：林绮蓓
- 发布时间：2026-10-13 17:57 CST
- 链接：https://www.infoq.cn/article/LQjytCZpPdgOE5PrWU59?utm_source=rss&utm_medium=article

### 3. Claude 开始自己写程序管理 Agent 了：Anthropic 披露动态工作流架构
- 摘要：点击查看原文>
- 作者：林绮蓓
- 发布时间：2026-10-13 17:41 CST
- 链接：https://www.infoq.cn/article/8La5gsJVOOF5BvFiLAUF?utm_source=rss&utm_medium=article

## IT之家（ithome，zh，本窗口共 110 条）

### 1. 赛力斯 & 字节合作：赛豆科技 AIVA 第二款车型预计为 SUV，考虑采用换电方案
- 摘要：IT之家 10 月 13 日消息，据蓝鲸新闻今日报道，赛豆科技旗下 AIVA 品牌的第二款车型预计为 SUV，并考虑采用换电方案。 知情人士透露，赛豆科技是否与宁德时代“巧克力换电”合作，目前最终方案尚未确定，“还没定义清楚”。 IT之家注：“巧克力换电”整体解决方案由宁德时代全资子公司时代电服科技有限公司推出。据宁德时代官方数据，截至 2026 年 9 月 29 日，巧克力换电全国累计建成换电站超 2520 座，站点覆盖 31 个省份、200 座城市，近 2 万块全新电池完成入仓部署。 赛豆科技的前身为重庆蓝电科技有限公司，今年 5 月底正式更名。赛力斯 2026 年中期报告显示，赛力斯以注...
- 作者：作者： 问舟
- 发布时间：2026-10-13 19:00 CST
- 链接：https://www.ithome.com/1/012/538.htm

### 2. AMD 首次展示 Verano 霄龙处理器：计划 2027 年上市，支持 LPDDR5X
- 摘要：IT之家 10 月 13 日消息，AMD 在当地时间 10 月 12 日开幕的 2026 OCP 全球峰会上首次公开展示了下一代 Verano 系列 EPYC 数据中心处理器。 该系列处理器计划于 2027 年推出，将采用 Zen 6 架构，并首次在 EPYC 产品线中支持 LPDDR5X 内存，通过 SOCAMM2 内存模块为面向智能体 AI 的数据中心提供端侧计算能力。 AMD CEO 苏姿丰在主题演讲中将 Verano 称为 AMD 面向 AI 时代的下一步 CPU 产品布局。该处理器主要面向 AI 加速器主机节点，计划与未来几代 AMD Instinct GPU 搭配使用，以满足智能体...
- 作者：作者： 问舟
- 发布时间：2026-10-13 18:54 CST
- 链接：https://www.ithome.com/1/012/535.htm

### 3. 千问 AI 耳夹式耳机开售：Bose 调音，到手价 1099 元
- 摘要：IT之家 10 月 13 日消息，千问 AI 耳夹式耳机现已在京东开售。新品主打 Bose 大师调音，支持 AI 笔记、AI 同声传译等功能，到手价 1099 元。 据介绍，这款耳机有深空蓝、星光色、极光紫三种颜色可选，不分左右耳，支持 IP55 级防尘防泼溅，至多可配对 8 台设备，支持双设备同时连接；耳机续航 9 小时，配合充电仓 40 小时，支持无线充电。 这款耳机搭载 0.5mm 超薄记忆钛丝，专为亚洲人耳打造；由 Bose 调音，专为耳夹式开放形态优化；支持动态 EQ，可随音量自动调整频率响应。 该耳机搭载 12 磁铁双环聚磁单元，支持 LHDC 5.0 高清蓝牙音频解码，最高可达...
- 作者：作者： 潞源
- 发布时间：2026-10-13 18:51 CST
- 链接：https://www.ithome.com/1/012/532.htm

## 雷峰网（leiphone，zh，本窗口共 12 条）

### 1. 再发断轴事件！奇瑞官宣召回马来西亚市场OMODA 5；汽车坠百米悬崖车主奇迹生还！车企回应；曝梁文锋密集接触具身智能创业者丨雷峰早报
- 摘要：要闻提示 1.再发断轴事件！奇瑞官宣召回马来西亚市场OMODA 5，国内开展同批次风险排查 2.汽车坠百米悬崖车主奇迹生还！车企回应 3.宇树王兴兴：我犯的最大错误是对AI相信得还不够 4.曝梁文锋密集接触具身智能创业者，DeepSeek拟入局具身智能 5.前优必选联席 CTO 廖洪涛入职腾讯福田实验室，任具身智能方向负责人 6.问界汽车计划明年进入欧洲市场，已启动欧盟整车型式认证工作 7.DUV光刻机榨到极限！长鑫G6内存面积再缩30%：键合工艺首次登场 8.扎克伯格押注“个人超级智能”！Meta宣布：推出新模型 今日头条 再发断轴事件！奇瑞官宣召回马来西亚市场OMODA 5，国内开展同批次...
- 发布时间：2026-10-13 14:21 CST
- 链接：https://www.leiphone.com/category/zaobao/sVMq5cHa4c52VolM.html

### 2. 其域创新以 62 亿个高斯、150 亿个点云，建成全球最大的空地一体 3D 高斯模型“闽宁镇”
- 摘要：它覆盖 23.5 平方公里，相当于 3291 个标准足球场，由 18.6 万张航拍与地面影像、150 亿个雷达点云训练而成，规模达 62 亿个高斯椭球。镇口的牌坊、红顶白墙的街区、通向远方的道路与山前转动的风机，都被收进了同一个连续的模型里。 这个模型，出现在中央广播电视总台重点纪录片《闽宁大道》中。从 8000 多人的闽宁村，到 6 万多人的移民示范镇，一座镇三十年的来路与今天的模样，就在这片可以自由穿行的数字空间里徐徐展开。 纪录片摄制组使用其域创新（XGRIDS）自主研发的空间采集设备与自主研发的软件，以及自主创新的大场景 3DGS 数据格式LCC，完成了这片区域的三维重建与可视化呈现。...
- 发布时间：2026-10-13 13:50 CST
- 链接：https://www.leiphone.com/category/industrynews/TvlYXDgobdGHyARw.html

### 3. 字节跳动 Seed 单独设立大模型安全与对齐部门
- 摘要：字节跳动 Seed 近日发出内部邮件，宣布将成立“Seed Model-Alignment&Preparedness”部门，由严林负责，汇报给 Seed 负责人吴永辉。原 Responsible AI 团队及部分 Chat 团队成员将转入新部门。 据悉，该部门的设立旨在加强安全与对齐方向的投入，对齐的核心是让模型的行为与人类意图和安全约束保持一致，从而提升 Agent Model（智能体模型）安全能力，以及防范 CBRN（化学、生物、放射、核）等前沿能力风险。 大模型安全风险正日益凸显，智能体逃逸引发的网络攻击等事件频繁发生。此前，国内大模型研究团队的安全与对齐工作大多被纳入到公司整体的安全合...
- 发布时间：2026-10-13 13:43 CST
- 链接：https://www.leiphone.com/category/industrynews/jX1ndNxDJ94n6bUu.html

## 开源中国（oschina，zh，本窗口共 11 条）

### 1. 倒计时3天！1016GOPS2026・上海站，参会指南请收好！
- 摘要：第 30 届智能体驱动的 GOPS 全球运维大会暨研运数智化峰会【1016~17】即将在上海火热开启，我们带着满满的诚意，邀您齐聚上海！ 2026 年智能体深度渗透 IT 各领域，如何紧抓行业变革黄金机遇，别让自己迷失在 AI 快速发展里？GOPS 您快了解下！这份 2 天盛会的“通关秘籍”快收好～带你沉浸式玩转 GOPS 大会盛宴。 一、会...
- 发布时间：2026-10-13 16:57 CST
- 链接：https://www.oschina.net/news/503001

### 2. Palantir CTO 上电视骂 AI 安全是“邪教”，还戏称 AI 研究者靠抽烟表信仰
- 摘要：Palantir 首席技术官 Shyam Sankar 在 CBS《Face the Nation》上抛出了几个惹火的判断。节目开头，主持人 Margaret Brennan 先甩了个民意数字：CBS 民调里 50% 的人认为 AI 带来的问题会多于解决的，45% 的美国人希望政府限制 AI 的研发和使用。他的回应不是顺着'该不该设护栏'谈，而是直接点名了一个他认为真正在背后操...
- 发布时间：2026-10-13 16:56 CST
- 链接：https://www.oschina.net/news/503000

### 3. 16个获奖名额，总奖池33万，“地心飞行”AIGC大赛全网征集创意视频
- 摘要：如果硬盘里正好躺着一部做完的超现实题材片子，或者你一直想用 AI 拍一段扣人心弦的冒险，现在有一场大赛正在等你的作品。 第四届开放原子大赛·2026 开源行业解决方案创新赛（下称北京开源创新赛）的赛道三，是「地心飞行」AIGC 创作赛道。它面向沉浸式飞行影院这类文旅场景，征集 2-5 分钟的超高清视频，主题围绕地底世...
- 发布时间：2026-10-13 16:42 CST
- 链接：https://www.oschina.net/news/502999

## 量子位（qbitai，zh，本窗口共 14 条）

### 1. 梁文锋投了Swin Transformer作者！DeepSeek开始布局具身大脑
- 摘要：Winverse AI
- 作者：量子位的朋友们
- 发布时间：2026-10-13 17:33 CST
- 链接：https://www.qbitai.com/2026/10/503093.html

### 2. 中国车企反攻德系车心脏！巴黎车展国产品牌独占三成，大众CEO连忙呼吁抱团迎战
- 摘要：宝马保时捷缺席
- 作者：杰西卡
- 发布时间：2026-10-13 15:20 CST
- 链接：https://www.qbitai.com/2026/10/502992.html

### 3. 华为哈勃投了个98年博士！让机器人皮肤变色，团队平均23岁
- 摘要：让材料感知压力，造出超薄高密度电子皮肤
- 作者：思邈
- 发布时间：2026-10-13 15:19 CST
- 链接：https://www.qbitai.com/2026/10/502954.html

## 少数派（sspai，zh，本窗口共 1 条）

### 1. 派早报：一加发布一加 16，Google 推出 Fitbit Edge 等
- 摘要：少数派的近期动态给电话加上「辅助驾驶」？我们想听听你的意见。我们将从提交的问卷中挑选40份用心回答，每份送出50元面值京东卡。参与调研能让AI助手通过自然语言指令直接与您的Quote/0摘录墨水屏交互 ... 查看全文
- 作者：少数派编辑部
- 发布时间：2026-10-13 08:01 CST
- 链接：https://sspai.com/post/116033

## 钛媒体（tmtpost，zh，本窗口共 58 条）

### 1. 千问借钉钉进场，靠什么留下？
- 摘要：文 | 新立场Pro 千问办公在云栖大会上介绍企业上下文时，举了一个古茗的案例。 门店员工想知道海报怎么贴，Agent需要找到品牌内部的操作规范。按照发布材料，古茗的飞书文档、知识库、答疑群和培训日程，被整理成门店运营知识空间。面对一个具体问题，系统提供的是相关资料，而非把全部运营知识都交给Agent。 古茗原来就在使用飞书， 千问办公想做企业生意，得想办法进入钉钉以外的工作环境。 三年前，钉钉已经开始尝试让AI进入企业业务。2023年8月，叶军在生态大会上提出“企业上下文”，希望大模型能够理解不同企业的内部规则。 9月22日，千问办公CEO陈宇森再次将上下文放到中心，演讲题目是“Contex...
- 作者：新立场Pro
- 发布时间：2026-10-13 18:43 CST
- 链接：https://www.tmtpost.com/8165804.html

### 2. AI闯入好莱坞：一家公司如何改写百年规则
- 摘要：MIPCOM（戛纳秋季电视节）的开场位置历来都是巨头制片厂的专属。 但在今年，10月13日，MIPCOM的开场演讲Grand Auditorium里，一家起源于硅谷的AI原生影视公司——Utopai，登上了主舞台并分享了它对影视行业未来的判断：AI原生制片厂正在从概念走向交付，围绕原创IP、人类创意和专有电影基础设施构建的新制片体系，将重新定义内容的生产与全球发行。 同样是在MIPCOM上，Utopai还释放了与韩国娱乐产业巨头CJ ENM Studios即将推进合作的信息。 安东尼奥·班德拉斯（Antonio Banderas）同日宣布出演电影《Cortés》的消息，正是在这个关键时间节点上...
- 作者：LCC_Beta版
- 发布时间：2026-10-13 18:25 CST
- 链接：https://www.tmtpost.com/8166842.html

### 3. 云深处IPO：不表演的机器人，靠什么放量？
- 摘要：文 | 市值榜，作者 | 陈智远，编辑 | 嘉辛 在春晚舞台表演、参加马拉松比赛中，机器人的技能越点越多，但这些技能如何和生活、生产结合在一起，以解放劳动力、提升生产力，才是这个产业接下来要回答的问题。 从优必选推出的情感陪伴机器人到梅卡曼德创始人邵天兰对于具身智能产品没有PMF（产品市场匹配）的抨击，关于机器人究竟应该用在什么地方，已经是一个热议的话题。 越来越多的观点认为，机器人首先应该替代的是高危工作、枯燥的工作、恶劣环境下的工作，应该是具身智能真正产生价值的地方，吟诗作对、娱乐表演等娱情遣兴的活动应该留给人。 云深处聚焦的就是前一类场景，它的四足和轮足机器人在变电站、灾害现场、矿山隧道...
- 作者：市值榜
- 发布时间：2026-10-13 18:23 CST
- 链接：https://www.tmtpost.com/8167181.html

## 智东西（zhidx，zh，本窗口共 5 条）

### 1. OpenAI弃子变棋子，Sora借初创公司复活
- 摘要：备选标题： 1、Sora将复活，OpenAI借初创公司杀回影视 2、OpenAI拟借初创公司复活Sora，重返AI影视 3、OpenAI拟移交Sora，初创定制后推向影视 4、OpenAI洽谈复活Sora，借初创公司重返影视 智东西 编译 | 黄菲 编辑 | 江宇 智东西10月13日报道，今日，科技媒体《The Information》报道称，OpenAI正与一家为电影人开发AI视频的隐秘初创公司谈判，计划让该初创公司获取并改造已停运的视频生成模型Sora，使Sora以专业影视工具或服务形式重新进入市场。 该初创公司尚未公开名称。《The Information》披露，其创始团队包括好莱坞资深...
- 作者：黄 菲
- 发布时间：2026-10-13 13:54 CST
- 链接：https://zhidx.com/p/600374.html

### 2. 干掉Fable 5.1！Meta甩出最强模型，即将上线Muse
- 摘要：智东西 作者 | 毕伟豪 编辑｜李水青 智东西10月13日报道，昨夜，Meta发布了首个 前沿模型系列Muse Wonder ，包括Muse Wonder和Muse Wonder Full两个型号，重点面向 个人与专业智能体任务 。 Meta CEO马克·扎克伯格发文称，Meta超级智能实验室成立至今已一年多，Muse Spark是团队推出的首个模型系列，此次推出的Muse Wonder系列规模更大、能力更先进，引领着Meta的模型能力迈入前沿水平。 2025年6月，扎克伯格重金组建超级智能团队，投百亿美元并购AI创企、狂揽顶尖AI人才，今日终于放出“大招”。今年4月份亮相的Muse Spar...
- 作者：毕 伟豪
- 发布时间：2026-10-13 13:05 CST
- 链接：https://zhidx.com/p/600299.html

### 3. 5699元起！一加16发布：全局165Hz、9000mAh电池、2亿像素主摄全来了
- 摘要：智东西 作者 | 杨京丽 编辑 | 李水青 智东西10月12日西安报道，刚刚，一加发布最新旗舰手机一加16。一加16搭载 第六代骁龙8超级至尊版 ，支持最高原生 185帧游戏体验 ，配备 9000mAh电池、第四代东方屏及2亿像素主摄 。 同时，一加16还配备自研 电竞网络芯片G3、超级显示芯片P4和灵犀触控芯片T3 ，搭配新一代 “冰河散热系统” 。充电方面，一加16支持 100W有线快充和50W无线快充 。 一加中国区总裁李杰在发布会上透露，2025年一加手机销量同比增长44%，增速位列行业第一，今年截至发布会前，一加手机销量 同比增长18% ，是目前手机行业 唯一保持两位数增长的品牌 。...
- 作者：杨 京丽
- 发布时间：2026-10-12 22:01 CST
- 链接：https://zhidx.com/p/600205.html

# Tier 3 — 社交 / 聚合

## GitHub Trending (daily)（github-trending，en，本窗口共 6 条）

### 1. open-webui/open-webui
- 摘要：User-friendly AI Interface (Supports Ollama, OpenAI API, ...) https://openwebui.com Open WebUI 👋 Open WebUI is a home for AI , a self-hosted AI platform that's extensible , feature-rich , user-friendly, and built to run entirely offline . With support for Ollama and OpenAI-compatible APIs , it gives...
- 发布时间：2026-10-13 20:00 CST
- 链接：https://github.com/open-webui/open-webui

### 2. microsoft/BitNet
- 摘要：Official inference framework for 1-bit LLMs bitnet.cpp 📰 News 07/23/2026: 📣 We released VibeASR.cpp — a real-time multilingual ASR inference engine on CPU using BitNet I2_S quantization, achieving RTF Code ] [ Models ] [ Report ] 07/20/2026: 📣 We released BitNet-embedding-0.6B and BitNet-embedding-2...
- 发布时间：2026-10-13 20:00 CST
- 链接：https://github.com/microsoft/BitNet

### 3. Alishahryar1/free-claude-code
- 摘要：Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly) Quick Start · Providers · C...
- 发布时间：2026-10-13 20:00 CST
- 链接：https://github.com/Alishahryar1/free-claude-code

## Hacker News (AI stories)（hackernews-ai，en，本窗口共 130 条）

### 1. An hour of audio transcribed in about 13s on MacBook Air
- 摘要：An embedding model, turned into a speech-to-text model. An hour of audio in about 13 seconds on a base MacBook Air, on device.
- 作者：amrrs
- 发布时间：2026-10-13 19:27 CST
- 链接：https://eg2.haku.sh/

### 2. Character.ai Files for Bankruptcy
- 摘要：The chatbot startup is looking to sell its assets to Disney after years of legal challenges and safety concerns.
- 作者：yanis_t
- 发布时间：2026-10-13 19:24 CST
- 链接：https://www.theverge.com/ai-artificial-intelligence/1009802/character-ai-files-for-bankruptcy-disney

### 3. Veda: The Agentic Hobby OS Added Video Player
- 摘要：Videos plays the videos in ~/Videos and any video opened from Files, the Terminal or the desktop: a library with a picture, length and size of each and "Continue watching", and a player w...
- 作者：vahmohhh
- 发布时间：2026-10-13 18:56 CST
- 链接：https://github.com/vahmoh25/Veda/commit/e8d3fdbce82a1d09db7dd0d182411e29772c0bc4

## Product Hunt — AI（producthunt-ai，en，本窗口共 21 条）

### 1. The Drive AI
- 摘要：The AI agent that does the work on your files Discussion | Link
- 作者：Bigyan Karki
- 发布时间：2026-10-13 13:39 CST
- 链接：https://www.producthunt.com/products/the-drive-ai-2

### 2. Toby
- 摘要：Realistic mock interviews with an AI hiring manager Discussion | Link
- 作者：Rob Kealey
- 发布时间：2026-10-13 10:51 CST
- 链接：https://www.producthunt.com/products/toby-5

### 3. HarnessHive
- 摘要：AI-Native, Simple & Collaborative Wire Harness Design Discussion | Link
- 作者：Daniel Kopelke
- 发布时间：2026-10-13 10:17 CST
- 链接：https://www.producthunt.com/products/harnesshive

## Reddit AI subreddits (hot)（reddit-ai-hot，en，本窗口共 30 条）

### 1. Do any local models come close to chatgpts ability to generate sample character images? (2nd image is original)
- 摘要：Quick note, not my character, original came from schmede_AI on youtube. But yes my question is do any local models currently have the ability to match and generate additional images of a character from a single reference image as well as this? I have tried a couple (Qwen Image 2.1 for example) out o...
- 作者：tammy_orbit
- 发布时间：2026-10-13 12:01 CST
- 链接：https://www.reddit.com/gallery/1x4ms5d

### 2. Krea3... incoming?
- 摘要：https://preview.redd.it/mi5kwjxpq5vh1.png?width=620&format=png&auto=webp&s=f059f48d28349d4b141bf265982567a0faf8564a https://x.com/krea_ai/status/2109661957150347685
- 作者：ArttTaku
- 发布时间：2026-10-13 11:55 CST
- 链接：https://www.reddit.com/r/StableDiffusion/comments/1x4mnzj/krea3_incoming/

### 3. Looped Diffusion Transformer: the same blocks run several times inside each denoising step, and loop depth can be changed at sampling time [R]
- 摘要：Paper: Looped Diffusion Transformer (arXiv 2609.40305, 30 Sep). Instead of making a text-to-image DiT bigger, it runs a shared group of transformer blocks several times inside each denoising step. The authors report that naive looping doesn't reliably help, and fix it with deep supervision on every...
- 作者：Fit-Ant2238
- 发布时间：2026-10-13 02:13 CST
- 链接：https://i.redd.it/fxhov56wu2vh1.png

## Reddit AI subreddits (new)（reddit-ai-new，en，本窗口共 359 条）

### 1. I'm building a cozy game with Claude
- 摘要：This is just a quick screen record of the game in its current state! I did make a shorter, slicker demo at first, but I would rather share the actual game such as it is. I hope you like it! I started creating with Sol some weeks back, then Astra, then started using Claude when 5.5 came out (bc Astra...
- 作者：ronrirem
- 发布时间：2026-10-13 19:58 CST
- 链接：https://v.redd.it/6je96tjy48vh1

### 2. [UPDATE] I Built a O(NlogN) attention system that retains 97% accuracy over long context (MQAR) [P]
- 摘要：ALHR- Adaptive learnable Hierarchical Routing is a static binary tree based system that uses learnable functions to REDUCE the amount of keys used. It takes less memory and SCALES much better VRAM with tokens I’ve also been testing tiny stories and it looks promising However i can’t post any present...
- 作者：Alarming-Emotion-894
- 发布时间：2026-10-13 19:52 CST
- 链接：https://www.reddit.com/r/MachineLearning/comments/1x4uk6i/update_i_built_a_onlogn_attention_system_that/

### 3. Horsey challenge | Strata Fork | Qwen 3.8 FN NVFP4
- 摘要：So I wanted to try the horsey challenge myself on the latest engine i been testing which is a strata fork by sergqwer. https://github.com/sergqwer/strata-nvfp4 . I seen a post earlier and seen i believe it was a iq3 i think and it was pretty dope so i thought i try out the NVFP4. I wasn't expecting...
- 作者：Beneficial-Ad-8127
- 发布时间：2026-10-13 19:50 CST
- 链接：https://v.redd.it/86e9phi2v7vh1

## 智源社区（baai-hub，zh，本窗口共 18 条）

### 1. GPT-6.1 Sol一夜扩容500k！完全免费
- 摘要：新智元报道 GPT-6.1 Sol，默认上下文直接冲到 500k ！ OpenAI Day 7更新，把Codex和ChatGPT Work里的默认窗口从272k扩到500k，一口气涨了约80%。 紧接着，Tibo又补了一刀： 用订阅额度跑GPT-6.1 Sol，不收长上下文附加费。 任务照常消耗订阅额度，但不再因为上下文变长，额外加收一笔。 通过API调用，仍按API价格表计费。 然而，开发者Mhmd Hammoud却在评论区反问：「现在改个配置，也算一次真正的升级了？」 GPT-6.1 Sol狂飙500k 许愿成功 在默认500k放出之前，开发者Lasse早就受够了等压缩。 他曾吐槽， Co...
- 作者：新智元
- 发布时间：2026-10-13 19:50 CST
- 链接：https://hub.baai.ac.cn/view/58633

### 2. 让隐私计算从“能算”到“好算”：SDH 分析套件工程化实践
- 摘要：在上一篇《SDH PaaS 3.0 全链路解析》中，我们提到：SDH 通过合作空间、数据资产管理、元数据隐私配置、分析套件创编、联邦学习引擎、实例执行、运行观测和结果交付，把“主体可识别、资产可约束、任务可确认、运行可追溯、结果可控制”的管理要求落到了完整协作链路。 其中， 分析套件 是让SDH营销分析能力从「可自操」迈向「规模化自操」的关键一环。如果说自定义 MPC SQL 是面向技术专家的“手动挡”，那么分析套件就是让更多业务运营同学也能上手的“自动挡”，它把营销场景里高频、标准的分析逻辑沉淀成可复用的组件模板，用户只需在表单里选择业务选项，系统就在后台完成 SQL改写、合法性校验、任务编...
- 作者：阿里妈妈技术
- 发布时间：2026-10-13 19:00 CST
- 链接：https://hub.baai.ac.cn/view/58632

### 3. Anthropic放手，亚马逊想买！帮AI「换芯片」，凭什么值70亿美元？
- 摘要：新智元报道 刚刚，亚马逊曝出一笔约70亿美元的AI收购！ 10月11日，《华尔街日报》援引知情人士称，亚马逊正在洽购AI创业公司Decart，潜在交易估值约70亿美元。 这家公司的绝活，是帮AI用上不同厂商的芯片，还能把这些芯片的算力用得更足。 在此之前，Anthropic也盯上了它。 彭博社9月报道称，双方曾探讨约60亿美元的交易，但Anthropic做完尽职调查后，决定不再推进。 Anthropic这边刚退出，亚马逊那边又坐上了谈判桌。 要知道，今年5月英伟达投资Decart时，这家公司的估值还接近40亿美元。 短短数月，潜在收购估值已升至约70亿美元。 一家帮AI「换芯片」的公司，凭什么...
- 作者：新智元
- 发布时间：2026-10-13 17:30 CST
- 链接：https://hub.baai.ac.cn/view/58631

---
共列出 127 条（窗口内采集总数 1090 条，来自 51 个信源）

## OpenClaw 推送提示
请基于本文件生成中文 Daily AI News 推送，不要联网，不要抓原文，不要扩展搜索。
优先 Tier 1 一手来源和国内外媒体中被多个信源同时报道的事件；Tier 3 社交条目只做补充。
每日只保留最新内容，覆盖更新。
