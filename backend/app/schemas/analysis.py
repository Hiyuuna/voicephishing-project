from datetime import datetime
from typing import List

from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    text: str


class AnalysisResponse(BaseModel):
    risk_score: float
    risk_level: str
    detected_keywords: List[str]
    analysis_method: str


class HistoryResponse(BaseModel):
    id: int
    input_text: str
    processed_text: str | None
    risk_score: float
    risk_level: str
    detected_keywords: str | None
    analysis_method: str
    created_at: datetime

    class Config:
        from_attributes = True