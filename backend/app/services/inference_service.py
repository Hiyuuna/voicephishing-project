from app.services.preprocessing import preprocess_text
from app.services.risk_scoring import calculate_rule_based_risk


def analyze_text(text: str):
    processed_text = preprocess_text(text)

    result = calculate_rule_based_risk(processed_text)

    return {
        "input_text": text,
        "processed_text": processed_text,
        "risk_score": result["risk_score"],
        "risk_level": result["risk_level"],
        "detected_keywords": result["detected_keywords"],
        "analysis_method": "rule_based",
    }