# 민승빈 (Seungbin Min)

[English](README.en.md)

<!-- ┌───────────────────────────────────────────────────────────────
     │ ① 소개 한 줄 — 아래 3개 중 하나를 골라 이 주석 밖으로 옮기세요.
     │    (지금 밖에 나와 있는 건 A안입니다. 바꾸려면 A를 지우고 붙여넣기)
     │
     │ B안 — 만든 것 중심
     │ 백테스트 엔진과 투자판단 도구를 만들었습니다. 지금은 국내 증권사
     │ 시세를 붙이는 중입니다.
     │
     │ C안 — 관심 중심
     │ 돈이 오가는 시스템의 백엔드에 관심이 있습니다. 틀렸을 때 티가 나는
     │ 코드를 좋아합니다.
     │
     │ D안 — 직접 쓰기 (면접에서 "본인 소개 한 줄로 해보세요"에 답할 말)
     │ ______________________________________________
     │
     │ ※ 고르고 나면 이 주석 블록은 통째로 지우세요.
     └─────────────────────────────────────────────────────────────── -->

핀테크 백엔드를 주력으로, 데이터·LLMOps를 겸합니다. HKU 데이터사이언스·엔지니어링 전공.
시장 데이터를 다루는 백엔드를 만듭니다.

## 프로젝트

**QuantPilot** — 암호화폐 백테스트 엔진 (비공개)
OKX 가격 캔들과 funding rate를 SQLite에 증분 수집하고, 전략을 돌려 성과를 재는 CLI.
수집은 idempotent해서 재실행하면 새 데이터만 붙습니다. 마지막 N개월을 OOS로 떼어내 과최적화를 드러냅니다.
public 데이터만 쓰므로 API 키가 필요 없습니다.
`Python` `SQLite`

**[MarketResearch](https://github.com/inpilot-dev/MarketResearch)** — 미국 주식 투자판단 도구
매수 전 체크 → 결정 스냅샷 → 사후 복기까지 기록하는 웹앱.
`openapi.yaml`을 서비스 간 계약의 단일 진실원으로 두고 web/api를 분리한 모노레포.
`Next.js` `FastAPI` `Supabase` `pgvector`

**[reviewPaper](https://github.com/inpilot-dev/reviewPaper)** — 논문 학습 챗봇
전자현미경 리뷰 논문을 근거 인용과 함께 답하고, 개념 그래프·간격 반복 퀴즈를 붙였습니다.
프런트엔드는 빌드 도구 없는 단일 HTML.
`FastAPI` `Claude API` `Docker`

**[prompt-forge](https://github.com/inpilot-dev/prompt-forge)** — 프롬프트 재작성 스킬
거칠게 쓴 프롬프트를 패턴 라이브러리 기반으로 다시 짭니다. 실행은 하지 않고 텍스트만 냅니다.
`Python`

그 외: [seungbin-dev](https://github.com/inpilot-dev/seungbin-dev) (기술 블로그, Next.js·MDX) · [AXHackathon](https://github.com/inpilot-dev/AXHackathon)

<!-- ② "매일 돌리는 것" 섹션 — 자랑조라 한 줄로 줄였습니다.
     통째로 빼고 싶으면 아래 두 줄(## 매일 ~ 올립니다.)을 지우면 됩니다.
     원래 길게 쓴 버전이 필요하면 git log로 이전 커밋에서 꺼내 쓰세요. -->

## 매일 돌리는 것

학습 팩 8개가 매일 카드를 한 장씩 발행합니다. 읽고 자기설명을 쓰면 커밋이 남고, 실제로 써먹은 개념만 지식 베이스로 올립니다.

## 스택

Python · FastAPI · SQLite · PostgreSQL/Supabase · TypeScript · Next.js · Docker · Vercel · Claude API
현재 학습 중: Kotlin · Spring · Kafka

<!-- 스택은 "실제 리포에 있는 것"만 남긴 상태입니다.
     추가할 때 기준: 그 기술로 만든 게 이 프로필에서 클릭 가능한가?
     아니면 넣지 마세요 (배지 부풀리기로 읽힙니다). -->

## 연락

alstmdqls03@gmail.com · [블로그](https://alstmdqls03-ux.github.io/)
