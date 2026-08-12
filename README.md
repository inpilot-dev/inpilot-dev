# 민승빈 (Seungbin Min)

[English](README.en.md)

핀테크 백엔드를 주력으로, 데이터·LLMOps를 겸합니다. HKU 데이터사이언스·엔지니어링 전공.
시장 데이터를 수집·검증하는 백엔드와, 그 위에 붙는 LLM 파이프라인을 만듭니다.

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

## 매일 돌리는 것

학습 팩 8개(코딩테스트·CS 개념·코드 리딩·DB 설계·백엔드·데이터사이언스·시스템 디자인·영어)가
매일 카드를 한 장씩 발행합니다. 읽고 자기설명을 쓰면 그날 커밋이 남고,
실제로 써먹은 개념만 개인 지식 베이스로 올립니다.

## 스택

Python · FastAPI · SQLite · PostgreSQL/Supabase · TypeScript · Next.js · Docker · Vercel · Claude API
현재 학습 중: Kotlin · Spring · Kafka

## 연락

alstmdqls03@gmail.com · [블로그](https://alstmdqls03-ux.github.io/)
