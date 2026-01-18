from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.router import router
from pathlib import Path

# uvicorn app.main:app --reload


app = FastAPI()
app.include_router(router)

BASE_DIR = Path(__file__).resolve().parent
print("BASE_DIR", BASE_DIR)
INDEX_FILE = BASE_DIR / "index.html"
print("INDEX_FILE", INDEX_FILE)

@app.get("/", include_in_schema=False, response_class=HTMLResponse)
def root():
    return INDEX_FILE.read_text(encoding="utf-8")
