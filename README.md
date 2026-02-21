# hey, i'm yigit

san francisco · been online since '97 · building ai tools

> in 2021 a friend showed me the first gpt playground and i was completely blown away. shifted my whole career from marketing to ai. now i just build stuff — CLIs, MCP servers, n8n nodes, tauri apps, deno sdks. whatever the problem needs.

## 🏗 systems & hardware

- **[cli-batch-requester](https://github.com/yigitkonur/cli-batch-requester)** — 10k+ req/s batch api client for llm endpoints — rust, async, load-balanced
- **[proxy-http-forward](https://github.com/yigitkonur/proxy-http-forward)** — high-performance http/https forward proxy in go — fasthttp, prometheus, zero fingerprint
- **[lib-osmo-ble](https://github.com/yigitkonur/lib-osmo-ble)** — reverse-engineered ble protocol for dji osmo pocket 3 — node.js, no app needed
- **[tauri-plugin-key-intercept](https://github.com/yigitkonur/tauri-plugin-key-intercept)** — tauri plugin to intercept macos system shortcuts via cgeventtap
- **[cli-disable-mic](https://github.com/yigitkonur/cli-disable-mic)** — stop airpods from stealing your mac's microphone — coreaudio daemon, zero cpu
- **[proxy-http-cache](https://github.com/yigitkonur/proxy-http-cache)** — transparent http cache proxy with redis — deduplicate api calls, save costs
- **[cli-dataflow-decompress](https://github.com/yigitkonur/cli-dataflow-decompress)** — bulk decompress files in gcs — apache beam pipeline, java + python
- **[alfred-menubar-pin](https://github.com/yigitkonur/alfred-menubar-pin)** — pin a reminder to your macos menu bar with alfred and bitbar

## 🤖 ai & llm

- **[api-llm-ocr](https://github.com/yigitkonur/api-llm-ocr)** — pdf to markdown using vision llms — tables, layouts, and structure preserved
- **[cli-continues](https://github.com/yigitkonur/cli-continues)** — resume any ai coding session in another tool — claude code, copilot, gemini, codex, cursor
- **[cli-bulk-caller](https://github.com/yigitkonur/cli-bulk-caller)** — bulk outbound calls with automatic whisper transcription via telnyx
- **[cli-localize](https://github.com/yigitkonur/cli-localize)** — ai-powered localization cli — srt, json, po, xml, arb with token-aware batching
- **[notebook-hdbscan](https://github.com/yigitkonur/notebook-hdbscan)** — cluster text embeddings with dbscan and hdbscan — parameter sweep, excel export
- **[cli-finetune-dataset](https://github.com/yigitkonur/cli-finetune-dataset)** — weighted category-balanced dataset builder for llm fine-tuning
- **[cli-subtitle-linter](https://github.com/yigitkonur/cli-subtitle-linter)** — netflix-compliant subtitle fixer — syllable-weighted timing, auto line balancing

## 🔌 mcp servers

- **[mcp-research-powerpack](https://github.com/yigitkonur/mcp-research-powerpack)** — mcp server for deep research — google, reddit, scraping, and ai synthesis
- **[mcp-better-vibe-kanban](https://github.com/yigitkonur/mcp-better-vibe-kanban)** — mcp server for vibe kanban — manage tasks and sessions from your ai editor
- **[mcp-latitude-prompts](https://github.com/yigitkonur/mcp-latitude-prompts)** — mcp server for latitude.so — manage, sync, and run prompts from your ai editor
- **[mcp-parasut](https://github.com/yigitkonur/mcp-parasut)** — unofficial paraşüt sdk and mcp server — turkish accounting, invoices, e-fatura

reference implementations for every mcp transport pattern:

- **[example-mcp-stdio](https://github.com/yigitkonur/example-mcp-stdio)** — reference mcp server over stdio — every sdk feature demonstrated
- **[example-mcp-sse](https://github.com/yigitkonur/example-mcp-sse)** — reference mcp server over sse transport — calculator domain, teaching patterns
- **[example-mcp-stateless](https://github.com/yigitkonur/example-mcp-stateless)** — stateless mcp server — fresh instance per request, infinite horizontal scaling
- **[example-mcp-stateful](https://github.com/yigitkonur/example-mcp-stateful)** — stateful mcp server with redis sessions, event sourcing, and horizontal scaling

## 🛠 cli & developer tools

- **[cli-repo-to-prompt](https://github.com/yigitkonur/cli-repo-to-prompt)** — export any codebase to a single llm-ready markdown prompt
- **[cli-pr-consensus](https://github.com/yigitkonur/cli-pr-consensus)** — unify ai code review comments from one pr — copilot, coderabbit, bito, devin
- **[hooks-claude-code](https://github.com/yigitkonur/hooks-claude-code)** — auto-approve claude code plans instantly — optional craft.do archiving

## ⚙️ n8n ecosystem

- **[n8n-cli](https://github.com/yigitkonur/n8n-cli)** — full cli for n8n — manage workflows, validate json, diff, audit, all from terminal
- **[n8n-ffmpeg-stack](https://github.com/yigitkonur/n8n-ffmpeg-stack)** — n8n with ffmpeg and caddy ssl — docker compose, ready to deploy
- **[n8n-schema-generator](https://github.com/yigitkonur/n8n-schema-generator)** — auto-generated json schemas for every n8n node — hourly updates, validation api
- **[n8n-workflow-validator](https://github.com/yigitkonur/n8n-workflow-validator)** — validate n8n workflows using the actual n8n engine — catches what schemas miss
- **[n8n-node-boilerplate](https://github.com/yigitkonur/n8n-node-boilerplate)** — ai-optimized starter kit for building n8n community nodes
- **[n8n-nodes-craft](https://github.com/yigitkonur/n8n-nodes-craft)** — n8n community nodes for craft docs — blocks, tasks, collections, search
- **[n8n-nodes-latitude](https://github.com/yigitkonur/n8n-nodes-latitude)** — n8n node for latitude.so — run prompts, chat, and log conversations
- **[n8n-workflows-craft](https://github.com/yigitkonur/n8n-workflows-craft)** — 42 n8n workflows connecting craft docs with ai, rag, analytics, and more

## 🦕 deno sdks

- **[sdk-deno-serper](https://github.com/yigitkonur/sdk-deno-serper)** — type-safe deno client for serper.dev — 10 google search endpoints, zero deps
- **[sdk-deno-clado](https://github.com/yigitkonur/sdk-deno-clado)** — deno sdk for clado — linkedin search, profile enrichment, contact info
- **[sdk-deno-latitude](https://github.com/yigitkonur/sdk-deno-latitude)** — latitude sdk for deno and supabase edge functions — no node.js polyfills
- **[sdk-deno-mem0](https://github.com/yigitkonur/sdk-deno-mem0)** — deno sdk for mem0 — ai memory storage, semantic search, zero dependencies

## writing

- **[mcp server architecture: state management, security & tool orchestration](https://zeo.org/resources/blog/mcp-server-architecture-state-management-security-tool-orchestration)** + two more on observability and safety
- **[blog.yigitkonur.com](https://blog.yigitkonur.com)** — nfs vs smb for dev envs, claude code ssh remote, auto-approve plan mode, etc.

## talks

- [clickhouse](https://clickhouse.com/videos/how-we-used-clickhouse-to-create-lightning-fast-experiences-at-seodo) — how we used clickhouse for lightning fast experiences at seo.do
- [search'n stuff antalya](https://www.youtube.com/@searchnstuff/videos) — panel discussion (2025)
- [digitalzone istanbul](https://www.youtube.com/watch?v=a_OVqZlQT64) — from seo to ai: building tools with claude + gpt (2024)
- [search'n stuff antalya](https://www.youtube.com/playlist?list=PL5WYuC1ob3wCbOGJqUQilOCoHs_7qb3px) — building tools with claude 3.5 sonnet artifacts (2024)
- [brick institute](https://www.youtube.com/watch?v=s876vM5SL_A) — prompt engineering techniques for llms (2024)
- [digitalzone istanbul](https://www.youtube.com/watch?v=dMb1q6yyTW4) — ai-based new generation working culture (2023)
- [digitalzone istanbul](https://www.youtube.com/watch?v=11GoGouBY2Q) — mastering prompt engineering & ai integration (2023)
- [digitalzone istanbul](https://www.youtube.com/watch?v=Zwv1BFW2nQ0) — using chatgpt and gpt-3 apis for automation (2023)
- [consultancy days](https://www.youtube.com/watch?v=TX0PIL9TIOs) — effective use of ai for e-commerce (2023)
- [digitalzone istanbul](https://www.youtube.com/watch?v=y8On1RaT6Y4) — understanding bigquery for large-scale data (2021)
- [consultancy days](https://www.youtube.com/watch?v=Ou59MaqlmUM) — what we can learn from search console (2019)
- [digitalzone istanbul](https://www.youtube.com/watch?v=fv5wO9Ue7mo) — machine learning for search (2018)
- [brightonseo london](https://www.youtube.com/watch?v=yEwMQ1LQXxk) — connecting apis without coding skills (2017)
- [consultancy days](https://www.youtube.com/watch?v=dbNfqayHkV8) — seo & ppc team collaboration (2017)
- [digitalzone istanbul](https://www.youtube.com/watch?v=HhrA9Me8JAQ) — how to measure digital investments (2016)

## activity

[![github contribution graph](https://ghchart.rshah.org/yigitkonur)](https://github.com/yigitkonur)

## connect

[![twitter](https://img.shields.io/badge/-@yigitkonur-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/yigitkonur) [![linkedin](https://img.shields.io/badge/-yigit_konur-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yigitkonur/) [![github](https://img.shields.io/badge/-follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yigitkonur) [![blog](https://img.shields.io/badge/-blog-FF5722?style=flat-square&logo=hugo&logoColor=white)](https://blog.yigitkonur.com) [![youtube](https://img.shields.io/badge/-youtube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@yigitkonur)

---

- made my first website in '97 on a pentium ii — [see the recreation](https://yigitkonur.com)
- from izmir, lived in lisbon, now sf
