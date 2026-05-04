from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AnalysisLog(Base):
    __tablename__ = "analysis_logs"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(Text, nullable=False)
    processed_text = Column(Text, nullable=True)
    risk_score = Column(Float, nullable=False)
    risk_level = Column(String, nullable=False)
    detected_keywords = Column(Text, nullable=True)
    analysis_method = Column(String, nullable=False, default="rule_based")
    created_at = Column(DateTime, default=datetime.utcnow)