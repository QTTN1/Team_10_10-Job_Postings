"""Minimal FastAPI app: health checks only. Prediction/RAG endpoints get added later."""
from fastapi import FastAPI, HTTPException

from database.connection import get_connection

app = FastAPI(title="JobGuard API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/health/db")
def health_db() -> dict:
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("select 1")
            return {"status": "ok", "database": "reachable"}
    except Exception as exc:  # report, don't leak connection details
        raise HTTPException(status_code=503, detail=f"database unreachable: {type(exc).__name__}")
