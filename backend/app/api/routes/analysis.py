from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.crud import create_analysis_log
from app.db.database import SessionLocal
from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.services.inference_service import analyze_text

router = APIRouter(prefix="/analysis", tags=["Analysis"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest, db: Session = Depends(get_db)):
    result = analyze_text(request.text)

    create_analysis_log(db, result)

    return {
        "risk_score": result["risk_score"],
        "risk_level": result["risk_level"],
        "detected_keywords": result["detected_keywords"],
        "analysis_method": result["analysis_method"],
    }