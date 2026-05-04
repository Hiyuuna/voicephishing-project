from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.crud import delete_analysis_log, get_analysis_log, get_analysis_logs
from app.db.database import SessionLocal
from app.schemas.analysis import HistoryResponse

router = APIRouter(prefix="/history", tags=["History"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[HistoryResponse])
def read_history(db: Session = Depends(get_db)):
    return get_analysis_logs(db)


@router.get("/{log_id}", response_model=HistoryResponse)
def read_history_detail(log_id: int, db: Session = Depends(get_db)):
    log = get_analysis_log(db, log_id)

    if log is None:
        raise HTTPException(status_code=404, detail="분석 기록을 찾을 수 없습니다.")

    return log


@router.delete("/{log_id}")
def remove_history(log_id: int, db: Session = Depends(get_db)):
    log = delete_analysis_log(db, log_id)

    if log is None:
        raise HTTPException(status_code=404, detail="삭제할 기록을 찾을 수 없습니다.")

    return {"message": "삭제 완료"}