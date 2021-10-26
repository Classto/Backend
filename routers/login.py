from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Request, HTTPException

from json.decoder import JSONDecodeError

login_router = InferringRouter()


@cbv(login_router)
class Login:
    @login_router.post("/login/{application}")
    async def get_user(self, application: str, request: Request):
        try:
            data = await request.json()
        except JSONDecodeError:
            raise HTTPException(status_code = 400, detail = "Bad Request")

        return {"request" : data, "application" : application}

    @login_router.post("/register")
    async def register(self, request: Request, application: str):
        pass        
