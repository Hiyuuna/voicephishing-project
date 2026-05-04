PHISHING_KEYWORDS = {
    "계좌": 20,
    "송금": 25,
    "이체": 25,
    "OTP": 20,
    "비밀번호": 25,
    "인증번호": 25,
    "검찰": 20,
    "경찰": 15,
    "금융감독원": 20,
    "대출": 10,
    "당장": 15,
    "지금 바로": 20,
    "압수": 20,
    "수사": 15,
}


def calculate_rule_based_risk(text: str):
    score = 0
    detected_keywords = []

    for keyword, weight in PHISHING_KEYWORDS.items():
        if keyword in text:
            score += weight
            detected_keywords.append(keyword)

    score = min(score, 100)

    if score < 30:
        risk_level = "안전"
    elif score < 60:
        risk_level = "주의"
    elif score < 80:
        risk_level = "의심"
    else:
        risk_level = "위험"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "detected_keywords": detected_keywords,
    }