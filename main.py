from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse


BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = BASE_DIR / "cloud-engineer-hub.html"

app = FastAPI(title="Cloud Engineer Hub")


@app.get("/", include_in_schema=False)
async def root() -> FileResponse:
    return FileResponse(HTML_PATH)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

