from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import login_router, meeting_router #, user_router

app = FastAPI(
    name="classto-backend",
    description="manage your life during COVID-19 better",
    version="0.0.1",
    docs_url="/docs"
)
app.include_router(login_router)
app.include_router(meeting_router)

origins = [
    "http://localhost:3000",
    "http://classto.net",
    "https://classto.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(User.router)

@app.get("/")
async def main():
    return { "code": 200, "status": "Hello World" }

uvicorn.run(app, host="0.0.0.0", port=5000)
