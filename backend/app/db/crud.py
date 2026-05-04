from sqlalchemy.orm import Session

from app.models.analysis_log import AnalysisLog


def create_analysis_log(db: Session, result: dict):
    log = AnalysisLog(
        input_text=result["input_text"],
        processed_text=result["processed_text"],
        risk_score=result["risk_score"],
        risk_level=result["risk_level"],
        detected_keywords=",".join(result["detected_keywords"]),
        analysis_method=result["analysis_method"],
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log


def get_analysis_logs(db: Session):
    return db.query(AnalysisLog).order_by(AnalysisLog.id.desc()).all()


def get_analysis_log(db: Session, log_id: int):
    return db.query(AnalysisLog).filter(AnalysisLog.id == log_id).first()


def delete_analysis_log(db: Session, log_id: int):
    log = get_analysis_log(db, log_id)

    if log is None:
        return None

    db.delete(log)
    db.commit()

    return log