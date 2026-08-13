# Seungbin Min

[한국어](README.md)

<!-- ┌───────────────────────────────────────────────────────────────
     │ ① 소개 한 줄 (영문) — 국문 README에서 고른 안과 짝을 맞추세요.
     │
     │ B안 — 만든 것 중심
     │ I've built a backtesting engine and an investment decision tool.
     │ Right now I'm wiring up Korean brokerage market data.
     │
     │ C안 — 관심 중심
     │ I'm interested in backends where money moves, and in code that
     │ tells you loudly when it's wrong.
     │
     │ ※ 고르고 나면 이 주석 블록은 통째로 지우세요.
     └─────────────────────────────────────────────────────────────── -->

Backend engineer focused on fintech, with data and LLMOps alongside it.
BEng in Data Science & Engineering, HKU.
I build backends that handle market data.

## Projects

**QuantPilot** — crypto backtesting engine (private)
A CLI that incrementally collects OKX price candles and funding rates into SQLite, then runs strategies against them.
Collection is idempotent — re-running only appends new data. The last N months are held out as out-of-sample to expose overfitting.
Uses public data only, so no API key is required.
`Python` `SQLite`

**[MarketResearch](https://github.com/inpilot-dev/MarketResearch)** — US equity decision tool
A web app that records the full cycle: a pre-purchase checklist, a snapshot of the decision, and a review after the outcome is known.
A monorepo that separates web and api, with `openapi.yaml` as the single source of truth for the contract between them.
`Next.js` `FastAPI` `Supabase` `pgvector`

**[reviewPaper](https://github.com/inpilot-dev/reviewPaper)** — study chatbot for research papers
Answers questions about electron microscopy review papers with citations, alongside a concept graph and spaced-repetition quizzes.
The frontend is a single HTML file with no build tooling.
`FastAPI` `Claude API` `Docker`

**[prompt-forge](https://github.com/inpilot-dev/prompt-forge)** — prompt rewriting skills
Rebuilds rough prompts from a pattern library. It only produces text, and never executes anything.
`Python`

Also: [seungbin-dev](https://github.com/inpilot-dev/seungbin-dev) (tech blog, Next.js + MDX) · [AXHackathon](https://github.com/inpilot-dev/AXHackathon)

<!-- ② 국문판과 동일하게 한 줄로 줄였습니다. 빼려면 아래 두 줄 삭제. -->

## Daily loop

Eight study tracks publish one card a day. Reading one and writing my own explanation of it produces a commit, and only the concepts I've actually used get promoted into my knowledge base.

## Stack

Python · FastAPI · SQLite · PostgreSQL/Supabase · TypeScript · Next.js · Docker · Vercel · Claude API
Currently learning: Kotlin · Spring · Kafka

## Contact

alstmdqls03@gmail.com · [Blog](https://alstmdqls03-ux.github.io/)
