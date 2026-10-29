<picture><source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg"><img src="assets/hero-light.svg" width="100%" alt="Seungbin Min — financial-data backends built with AI agents. HKU Data Science & Engineering, Hong Kong. Method: rules compute, the model judges, a human owns the doubt."></picture>

<p align="center"><samp><a href="https://inpilot.dev">blog</a> · <a href="mailto:alstmdqls03@gmail.com">email</a> · <a href="README.ko.md">한국어</a></samp></p>

I build backends for financial data with AI agents, and the checks that keep the agents honest.
**Rules do the arithmetic. The model does the judgment. A human owns the doubt.**

### Start here

<p>
  <a href="https://github.com/inpilot-dev/hacku-2026"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-mandate-dark.svg"><img src="assets/card-mandate-light.svg" width="49%" alt="Mandate — agent wallet, 23/23 attacks held"></picture></a>
  <a href="https://github.com/inpilot-dev/ledger-exceptions"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-ledger-exceptions-dark.svg"><img src="assets/card-ledger-exceptions-light.svg" width="49%" alt="ledger-exceptions — 15/15 breaks found, 0 false positives"></picture></a>
</p>
<p>
  <a href="https://github.com/inpilot-dev/prompt-forge"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-prompt-forge-dark.svg"><img src="assets/card-prompt-forge-light.svg" width="49%" alt="prompt-forge — 4 Claude Code skills"></picture></a>
  <a href="https://github.com/inpilot-dev/reviewPaper"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-reviewPaper-dark.svg"><img src="assets/card-reviewPaper-light.svg" width="49%" alt="reviewPaper — cited answers, gold-set eval gate"></picture></a>
</p>
<p>
  <a href="https://github.com/inpilot-dev/seungbin-dev"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-seungbin-dev-dark.svg"><img src="assets/card-seungbin-dev-light.svg" width="49%" alt="seungbin-dev — blog pipeline with an LLM grader"></picture></a>
  <a href="https://github.com/inpilot-dev/Research"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-research-dark.svg"><img src="assets/card-research-light.svg" width="49%" alt="Research · verify — checks cited sentences against their sources, 250 tests passing"></picture></a>
</p>

### How I work with agents

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/flow-dark.svg"><img src="assets/flow-light.svg" width="100%" alt="Grill until the spec is clear → spec → tickets → one fresh subagent per ticket, test first → gate of tests and evals (fail goes back) → human review."></picture>

- **Repeated work becomes a skill, not a longer prompt.** prompt-forge is public; 9 more skills live in a private Claude Code plugin.
- **Gates live in code.** A Stop hook keeps the agent from finishing while tests fail. Unattended runs get their write scope from `--allowedTools`, not from a sentence in the prompt.
- **Models don't do the math.** Balances, scores and card text are computed or drawn by code; the model judges and explains.
- **I write down what isn't proven.** Mandate's README has a "Not claimed" section. QuantPilot was shelved when every candidate strategy failed its walk-forward and random-control gates, so no real money was traded.

### Marketing a one-person company, automated

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/engine-dark.svg"><img src="assets/engine-light.svg" width="100%" alt="Content engine: daily digest, Claude drafts, a grader checks 20 voice rules, a human merges to publish. Live: blog, Threads. Built: Instagram carousel, 9:16 reels, shorts from long video, newsletter."></picture>

- **One topic in, six channels out.** A daily digest collects sources, Claude drafts, a grader checks 20 voice rules and that every number appears in the source, and merging the PR is the only publish button. Code: [seungbin-dev](https://github.com/inpilot-dev/seungbin-dev).
- **Live today:** the blog at [inpilot.dev](https://inpilot.dev) (45 posts, a new draft every Saturday) and Threads (a publish queue on Mon/Wed/Fri). All 32 daily-digest runs so far are green.
- **Built, not switched on yet:** Instagram carousels (1080×1350, text drawn by code), 9:16 reels (Remotion), a cutter that turns a long video into a 60-second short (Whisper + an LLM choosing which blocks stay), and a weekly newsletter (Resend). Each one stops at a dry run until I turn it on.

### What I can build

| Layer | What I've used | Where |
|---|---|---|
| Frontend | Next.js 16 · React · Vite · Tailwind · shadcn/Radix · MDX · offline PWA · Three.js | [inpilot.dev](https://inpilot.dev) · [hacku-2026](https://github.com/inpilot-dev/hacku-2026) · overload-log, char-kit *(private)* |
| Backend | FastAPI · Java 17 + Spring Boot (hexagonal, ArchUnit) · Node/Bun · serverless functions | [reviewPaper](https://github.com/inpilot-dev/reviewPaper) · [hacku-2026](https://github.com/inpilot-dev/hacku-2026) · order-ledger *(private)* |
| Data | PostgreSQL/Supabase · pgvector · SQLite · Oracle · event sourcing · Flyway migrations · Kafka · Redis | [ledger-exceptions](https://github.com/inpilot-dev/ledger-exceptions) · order-ledger, NutriCoach *(private)* |
| AI | Claude API (citations) · `claude -p` · Ollama · RAG · eval gates · MCP servers · browser agents · Claude Code skills, plugins, hooks | [Research](https://github.com/inpilot-dev/Research) · [reviewPaper](https://github.com/inpilot-dev/reviewPaper) · [hacku-2026](https://github.com/inpilot-dev/hacku-2026) · [prompt-forge](https://github.com/inpilot-dev/prompt-forge) |
| Automation | GitHub Actions · launchd daemons · Discord/Telegram bots · Playwright rendering · headless-Chrome PDF | [seungbin-dev](https://github.com/inpilot-dev/seungbin-dev) · brain-secretary, card-news *(private)* |
| Video & graphics | Remotion · generated SVG · canvas | motion *(private)* · [this README](scripts/build_svgs.py) |
| Infra | Docker/Compose · Vercel · Fly.io · GitHub Pages · CI | [reviewPaper](https://github.com/inpilot-dev/reviewPaper) (Fly.io) · [inpilot.dev](https://inpilot.dev) & [sector-weather](https://sector-weather.vercel.app) (Vercel) |
| Testing | pytest · JUnit 5 + Testcontainers · vitest · Playwright e2e · Z3 model checking · hand-mutated assertions | [hacku-2026](https://github.com/inpilot-dev/hacku-2026) · [Research](https://github.com/inpilot-dev/Research) · order-ledger *(private)* |
| Market data | OKX (ccxt) · Korea Investment Open API · Alpaca WebSocket · Polymarket | QuantPilot, sector-weather, order-ledger, polymarket-bot *(private)* |
| Mobile | SwiftUI | mofit-ios, an iOS prototype *(private)* |

<table><tr><td valign="top" width="58%">

**Latest writing** <sub>(Korean · updates daily from [RSS](https://inpilot.dev/rss.xml))</sub>

<!-- BLOG-POST-LIST:START -->
- [ipfs 호환을 끊고 QUIC 하나만 남겼다 — iroh 1.0까지의 설계 결정](https://inpilot.dev/posts/iroh-road-to-1-0-cuts)
- [봇 수익 인증 세 건을 숫자만 빼고 다시 읽었다 — Polymarket PnL이 증명하지 못하는 것](https://inpilot.dev/posts/polymarket-bot-pnl-proves-little)
- [&lt;think&gt; 태그가 아니라 effort 레벨이다 — 추론 모델의 계산 제어](https://inpilot.dev/posts/reasoning-effort-not-think-tag)
- [결과는 그대로 나왔는데 과정은 사라졌다 — GPT-6 Astra 러닝 루트 생성](https://inpilot.dev/posts/astra-running-route-compaction)
- [무료지만 최신이 아니다 — syndication 429 실측과 종량제 API v2](https://inpilot.dev/posts/x-crawling-429-pay-per-use)
<!-- BLOG-POST-LIST:END -->

</td><td valign="top" width="42%">

**Running privately**

- Personal OS: knowledge vault run by Claude Code, notes graded C1–C3, weekly review on launchd
- seungbin-plugin: grill → spec → tickets → build, Stop-hook test gate
- brain-secretary: stdlib-only briefing bot, 29 tests, mutation-tested
- card-news: topic → 8 cards, text drawn by code
- polymarket-bot: autonomous dev loop, a fresh headless Claude session per task, one commit each
- sector-weather: 4-week team experiment, sector index → treemap, LLM explanation, scored forecasts ([archive](https://sector-weather.vercel.app))

</td></tr></table>

<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/inpilot-dev/inpilot-dev/output/snake-dark.svg"><img src="https://raw.githubusercontent.com/inpilot-dev/inpilot-dev/output/snake.svg" width="100%" alt="Contribution graph eaten by a snake"></picture>

<sub>Images in this README are generated by [`scripts/build_svgs.py`](scripts/build_svgs.py). Numbers come from each linked repo, as of Oct 2026.</sub>
