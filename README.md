# 📞 Voice Phishing Detection Backend

보이스피싱 문자 및 통화 전사문을 분석하여
위험도를 판단하는 FastAPI 기반 백엔드 서버입니다.

---

## 🚀 주요 기능

* 텍스트 기반 보이스피싱 위험도 분석
* 분석 결과 자동 DB 저장 (SQLite)
* 분석 기록 조회 API 제공
* Swagger UI를 통한 API 테스트 지원

---

## 🧠 시스템 구조

```
Client (App / Web)
        ↓
FastAPI (API Layer)
        ↓
Inference Service (분석 로직)
        ↓
SQLite DB (분석 기록 저장)
```

---

## 📡 API 명세

### 1️⃣ 서버 상태 확인

```
GET /health/
```

---

### 2️⃣ 텍스트 분석

```
POST /analysis/
```

#### Request

```json
{
  "text": "검찰입니다. 계좌가 범죄에 연루되었습니다. 송금하세요."
}
```

#### Response

```json
{
  "risk_score": 85,
  "risk_level": "위험",
  "detected_keywords": ["계좌", "송금", "검찰"],
  "analysis_method": "rule_based"
}
```

---

### 3️⃣ 분석 기록 조회

```
GET /history/
```

---

## ⚙️ 실행 방법

### 1. 프로젝트 클론

```bash
git clone <repository_url>
cd voicephishing-project/backend
```

---

### 2. 가상환경 생성 및 활성화

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

---

### 4. 서버 실행

```bash
uvicorn app.main:app --reload
```

---

### 5. Swagger 접속

```
http://127.0.0.1:8000/docs
```

---

## 🗂️ 프로젝트 구조

```
backend/
├── app/
│   ├── api/          # API 라우터
│   ├── core/         # 설정 관리
│   ├── db/           # DB 연결 및 CRUD
│   ├── models/       # DB 모델
│   ├── schemas/      # 요청/응답 데이터
│   ├── services/     # 비즈니스 로직
│   └── main.py       # 서버 진입점
│
├── requirements.txt
└── .gitignore
```

---

## 💾 데이터베이스

* SQLite 사용
* 서버 실행 시 자동 생성 (`voicephishing.db`)
* 별도 설치 필요 없음

---

## 🔥 설계 포인트

* 분석 로직과 API를 분리하여 유지보수성 향상
* `inference_service`를 통해 ML 모델 확장 가능
* 초기에는 Rule-based 방식 사용 → 이후 ML 연동 가능

---

## 📌 향후 개선

* KoELECTRA 기반 NLP 모델 적용
* PostgreSQL로 DB 확장
* AWS EC2 배포
* 사용자 인증 및 계정 시스템 추가

---

## 👨‍💻 개발 환경

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---
