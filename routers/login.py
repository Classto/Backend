from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Request, HTTPException

from models import User

from json.decoder import JSONDecodeError
import requests

login_router = InferringRouter()


@cbv(login_router)
class Login:
    @login_router.post("/login/{application}")
    async def get_user(self, application: str, user: User):

        return {
            "user" : user,
            "application" : application,
            "session_id" : 1234
        }

    @login_router.post("/register")
    async def register(self, request: Request, application: str):
        pass        
