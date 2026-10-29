<picture><source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg"><img src="assets/hero-light.svg" width="100%" alt="Seungbin Min — financial-data backends built with AI agents. HKU Data Science & Engineering, Hong Kong. Method: rules compute, the model judges, a human owns the doubt."></picture>

<p align="center"><samp><a href="https://inpilot.dev">블로그</a> · <a href="mailto:alstmdqls03@gmail.com">메일</a> · <a href="README.md">English</a></samp></p>

AI 에이전트로 금융 데이터 백엔드를 만들고, 에이전트를 믿을 수 있게 하는 검사도 만듭니다.
**계산은 규칙이 한다. 판단은 모델이 한다. 의심은 사람이 맡는다.**

### 여기부터 보세요

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
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-private-dark.svg"><img src="assets/card-private-light.svg" width="49%" alt="Private systems — personal OS, Claude Code plugin, briefing bot"></picture>
</p>

### 에이전트와 일하는 방식

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/flow-dark.svg"><img src="assets/flow-light.svg" width="100%" alt="Grill until the spec is clear → spec → tickets → one fresh subagent per ticket, test first → gate of tests and evals (fail goes back) → human review."></picture>

- **반복되는 일은 긴 프롬프트가 아니라 스킬로 만든다.** prompt-forge는 공개했고, 스킬 9개가 비공개 Claude Code 플러그인에 더 있다.
- **게이트는 코드에 둔다.** 테스트가 실패하면 Stop 훅이 에이전트를 끝내지 못하게 막는다. 무인 실행의 쓰기 범위는 프롬프트 문장이 아니라 `--allowedTools`가 정한다.
- **숫자 계산은 모델에게 시키지 않는다.** 잔액·점수·카드 글자는 코드가 계산하거나 그린다. 모델은 판단하고 설명한다.
- **증명하지 못한 것은 적어 둔다.** Mandate README에는 "Not claimed" 절이 있다. QuantPilot은 후보 전략이 전부 walk-forward·무작위 대조 게이트를 통과하지 못해 접었고, 실제 돈은 넣지 않았다.

<table><tr><td valign="top" width="58%">

**최근 글** <sub>([RSS](https://inpilot.dev/rss.xml)에서 매일 갱신)</sub>

<!-- BLOG-POST-LIST:START -->
- [ipfs 호환을 끊고 QUIC 하나만 남겼다 — iroh 1.0까지의 설계 결정](https://inpilot.dev/posts/iroh-road-to-1-0-cuts)
- [봇 수익 인증 세 건을 숫자만 빼고 다시 읽었다 — Polymarket PnL이 증명하지 못하는 것](https://inpilot.dev/posts/polymarket-bot-pnl-proves-little)
- [`<think>` 태그가 아니라 effort 레벨이다 — 추론 모델의 계산 제어](https://inpilot.dev/posts/reasoning-effort-not-think-tag)
- [결과는 그대로 나왔는데 과정은 사라졌다 — GPT-6 Astra 러닝 루트 생성](https://inpilot.dev/posts/astra-running-route-compaction)
- [무료지만 최신이 아니다 — syndication 429 실측과 종량제 API v2](https://inpilot.dev/posts/x-crawling-429-pay-per-use)
<!-- BLOG-POST-LIST:END -->

</td><td valign="top" width="42%">

**비공개로 돌리는 것**

- 개인 OS: Claude Code가 운영하는 지식 볼트, 노트를 C1–C3으로 등급, launchd 주간 리뷰
- seungbin-plugin: grill → spec → tickets → build, Stop 훅 테스트 게이트
- brain-secretary: 표준 라이브러리만 쓰는 브리핑 봇, 테스트 29개, 뮤테이션 테스트
- card-news: 주제 한 줄 → 카드 8장, 글자는 코드가 그린다

</td></tr></table>

<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/inpilot-dev/inpilot-dev/output/snake-dark.svg"><img src="https://raw.githubusercontent.com/inpilot-dev/inpilot-dev/output/snake.svg" width="100%" alt="Contribution graph eaten by a snake"></picture>

<sub>Python · FastAPI · TypeScript · Next.js · Supabase/pgvector · SQLite · Docker · GitHub Actions · Vercel · Claude API · Ollama · Z3 — 배우는 중: Kotlin · Spring · Kafka. 이 README의 그림은 [`scripts/build_svgs.py`](scripts/build_svgs.py)가 만든다.</sub>
