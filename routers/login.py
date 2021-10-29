from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Request, HTTPException

from models import User
from app import SESSION, DATABASE

from json.decoder import JSONDecodeError
import requests

login_router = InferringRouter()

#로그인
#가입

@cbv(login_router)
class Login:
    @login_router.post("/auth/login")
    async def get_user(self, user: User):
        if not DATABASE.exits(user.email):
            raise HTTPException(404, detail="user not found")

        id = DATABASE.get_id(user.email)
        session_id = SESSION.new_session(user, id)

        return {
            "user" : user,
            "id" : id,
            "session_id" : session_id
        }

    @login_router.post("/auth/register")
    async def register(self, user: User):
        pass