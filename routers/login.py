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
        current_category = DATABASE.info(id)["current_category"]
        session_id = SESSION.new_session(user, id)

        return {
            "user" : user,
            "id" : id,
            "session_id" : session_id,
            "current_category" : current_category
        }

    @login_router.post("/auth/register")
    async def register(self, user: User):
        if DATABASE.exits(user.email):
            raise HTTPException(403, detail="email already used")

        is_valid = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params = {"email" : user.email}
        ).json()['status']

        if is_valid == "valid":
            id = DATABASE.register(user)

            return {
                "user" : user,
                "id" : id
            }
        else:
            raise HTTPException(400, detail="email not allowed")
        
