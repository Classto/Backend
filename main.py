from fastapi import FastAPI
import uvicorn

from routers import Login, Meeting, User

app = FastAPI(
    name="classto-backend",
    description="manage your life during COVID-19 better",
    version="0.0.1"
)
app.include_router(Login.router)
app.include_router(Meeting.router)
app.include_router(User.router)


@app.get("/")
async def main():
    return { "code": 200, "status": "Hello World" }

uvicorn.run(app, host="0.0.0.0", port=5000)
