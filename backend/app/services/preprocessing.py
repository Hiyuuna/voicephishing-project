def preprocess_text(text: str) -> str:
    text = text.strip()
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text