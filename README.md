<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1e3a8a,100:06b6d4&height=200&section=header&text=Seungbin%20Min&fontSize=54&fontColor=ffffff&fontAlignY=34&desc=Backend%20for%20Fintech%20%C2%B7%20Data%20%2F%20LLMOps&descAlignY=54&descSize=18" width="100%"/>

<div align="center">

<a href="https://alstmdqls03-ux.github.io/"><img src="https://img.shields.io/badge/Blog-seungbin.dev-06b6d4?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>
<a href="mailto:alstmdqls03@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<a href="https://github.com/inpilot-dev"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>

<br/>

**시장 데이터를 수집·검증해 의사결정으로 바꾸는 백엔드**,<br/>
그리고 **그 과정을 자동화하는 LLM 파이프라인**을 만듭니다.

<sub>HKU · BEng in Data Science & Engineering</sub>

</div>

<br/>

<div align="center">
  <img src="https://img.shields.io/badge/-%20-0f172a?style=flat-square" width="100%" height="2"/>
</div>

## 🧭 무엇을 만드는가

<table>
<tr>
<td width="33%" valign="top">

### 📈 금융 데이터
거래소 public API 수집 → 로컬 DB 적재 → 백테스트까지 **CLI 하나로**. 수집은 idempotent 증분, 검증은 OOS 분리.

</td>
<td width="33%" valign="top">

### 🤖 LLM 애플리케이션
RAG · 근거 인용 · 에이전트 워크플로우를 **실제로 굴러가는 서비스**로. 데모가 아니라 매일 쓰는 것.

</td>
<td width="33%" valign="top">

### ⚙️ 자동화
매일 돌아가는 파이프라인이 **스스로 콘텐츠를 발행하고 커밋**하게. 사람은 판단만.

</td>
</tr>
</table>

<br/>

## 🛠 기술 스택

<div align="center">

**Backend**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white" />

**Data**<br/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />

**Frontend**<br/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />

**Infra / AI**<br/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" />
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
<img src="https://img.shields.io/badge/Claude_API-D97757?style=for-the-badge&logo=anthropic&logoColor=white" />

</div>

<br/>

## 🚀 대표 프로젝트

<table>
<tr>
<td width="50%" valign="top">

### 📊 QuantPilot `private`
암호화폐 **백테스트 엔진**.

OKX 가격 캔들·funding rate를 SQLite에 **idempotent 증분 수집**하고, 마지막 N개월을 **OOS(out-of-sample)로 분리**해 과최적화를 드러내는 CLI.

```bash
quantpilot backtest --strategy rsi-mr \
  --symbol BTC-USDT-SWAP --oos-months 2
# → Train/OOS Sharpe·MaxDD·승률 + equity curve
```

`Python` `SQLite` `pandas` · API 키 불필요

</td>
<td width="50%" valign="top">

### 🧠 [reviewPaper](https://github.com/inpilot-dev/reviewPaper)
전자현미경 리뷰 논문 **학습 챗봇**.

근거 인용 답변 · 개념 그래프 · 간격 반복 퀴즈 · 노트. 프런트는 빌드 도구 없는 **단일 HTML**.

`FastAPI` `Claude API` `Docker`

<br/>

### 🔧 [prompt-forge](https://github.com/inpilot-dev/prompt-forge)
거친 프롬프트를 **검증된 패턴 기반 프롬프트**로 재작성하는 Claude Code 스킬 4종 + 패턴 라이브러리.

`Python` `Prompt Engineering`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💹 [MarketResearch](https://github.com/inpilot-dev/MarketResearch)
**Market Insight OS** — 미국 주식 개인 투자자를 위한 AI 투자판단 디버거.

매수 전 30초 체크 → 결정 스냅샷 → AI 복기 → 프로세스 품질 거울. `openapi.yaml`을 서비스 간 계약의 단일 진실원으로 두는 모노레포.

`Next.js 16` `FastAPI` `Supabase` `pgvector`

</td>
<td width="50%" valign="top">

### ✍️ [seungbin-dev](https://github.com/inpilot-dev/seungbin-dev)
AI 워크플로우·자동화·백엔드 **기술 블로그**.

`Next.js` `MDX`

<br/>

### 🏆 [AXHackathon](https://github.com/inpilot-dev/AXHackathon)
AX 인재전쟁 해커톤 산출물.

`Python` `HTML`

</td>
</tr>
</table>

<br/>

## 🔁 매일 돌리는 것

> 공부를 이벤트가 아니라 **파이프라인**으로 만들었습니다.

**8개 학습 팩**(코딩테스트 · CS 개념 · 코드 리딩 · DB 설계 · 백엔드 · 데이터사이언스 · 시스템 디자인 · 영어)이 매일 카드 한 장씩 자동 발행되고, 읽고 자기설명을 쓰면 그날 커밋이 남습니다. 실전에서 실제로 쓰인 개념만 개인 지식 베이스로 승격됩니다.

```
_raw 수집  →  요약·구조화  →  개념 노트  →  실전 사용 검증  →  포트폴리오
```

<br/>

## 🎯 지금

| | |
|---|---|
| 🔭 **만드는 중** | QuantPilot 전략 정합성 검증 모듈 + 국내 증권사 시세 연동 |
| 🌱 **배우는 중** | Kotlin · Spring · Kafka — 결제/트레이딩 도메인 백엔드로 확장 |
| 🤝 **찾는 것** | 핀테크 백엔드 엔지니어 포지션 (한국 · 홍콩 이중 트랙) |
| 💬 **말 걸기** | 백테스트 · RAG · 개발 자동화 — 뭐든 환영입니다 |

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:06b6d4,50:1e3a8a,100:0f172a&height=120&section=footer" width="100%"/>
