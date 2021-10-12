from fastapi import FastAPI
import uvicorn

from routers import Login, Meeting

app = FastAPI(
    name="classto-backend",
    description="manage your life during COVID-19 better",
    version="0.0.1"
)

@app.get("/")
async def main():
    return { "code": 200, "status": "Hello World" }

uvicorn.run(app, host="0.0.0.0", port=5000)
