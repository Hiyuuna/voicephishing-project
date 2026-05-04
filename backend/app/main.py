from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import analysis, health, history
from app.db.database import engine
from app.models.analysis_log import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Voice Phishing Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(analysis.router)
app.include_router(history.router)


@app.get("/")
def root():
    return {"message": "Voice Phishing Detection API"}