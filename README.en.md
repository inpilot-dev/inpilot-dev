# Seungbin Min

[한국어](README.md)

Backend engineer focused on fintech, with data and LLMOps on the side.
BEng in Data Science & Engineering, HKU.
I build backends that collect and validate market data, and the LLM pipelines that sit on top of them.

## Projects

**QuantPilot** — crypto backtesting engine (private)
A CLI that incrementally collects OKX price candles and funding rates into SQLite, then runs strategies against them.
Collection is idempotent, so re-running only appends new data. The last N months are held out as out-of-sample to expose overfitting.
Uses public data only, so no API key is needed.
`Python` `SQLite`

**[MarketResearch](https://github.com/inpilot-dev/MarketResearch)** — US equity decision tool
A web app that records the whole loop: pre-purchase checklist, decision snapshot, and after-the-fact review.
A monorepo splitting web and api, with `openapi.yaml` as the single source of truth for the contract between them.
`Next.js` `FastAPI` `Supabase` `pgvector`

**[reviewPaper](https://github.com/inpilot-dev/reviewPaper)** — study chatbot for research papers
Answers questions about electron microscopy review papers with inline citations, plus a concept graph and spaced-repetition quizzes.
The frontend is a single HTML file with no build tooling.
`FastAPI` `Claude API` `Docker`

**[prompt-forge](https://github.com/inpilot-dev/prompt-forge)** — prompt rewriting skills
Rebuilds rough prompts using a pattern library. It only emits text and never executes anything.
`Python`

Also: [seungbin-dev](https://github.com/inpilot-dev/seungbin-dev) (tech blog, Next.js + MDX) · [AXHackathon](https://github.com/inpilot-dev/AXHackathon)

## Daily loop

Eight study tracks (algorithms, CS fundamentals, code reading, DB design, backend, data science, system design, English)
each publish one card a day. Reading a card and writing my own explanation of it leaves a commit,
and only the concepts I've actually used get promoted into my knowledge base.

## Stack

Python · FastAPI · SQLite · PostgreSQL/Supabase · TypeScript · Next.js · Docker · Vercel · Claude API
Currently learning: Kotlin · Spring · Kafka

## Contact

alstmdqls03@gmail.com · [Blog](https://alstmdqls03-ux.github.io/)
