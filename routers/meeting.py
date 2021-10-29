from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException

from app import SESSION, DATABASE

meeting_router = InferringRouter()

#미팅업데이트
#카테고리업데이트
#미팅가져오기
#카테고리가져오기

def get_user(id):
    session = SESSION.find(id)
    if session == ():
        raise HTTPException(404, detail="user not found")

    user = DATABASE.info(session[0])

    return user

@cbv(meeting_router)
class Meeting:
    @meeting_router.get("/schedule/{id}")
    async def get_meeting(self, id: int):
        user = get_user(id)
        schedule = DATABASE.search(user.id, DATABASE.SCHEDULE)

        return {
            "id" : id,
            "data" : schedule
        }

    @meeting_router.get("/category/{id}")
    async def get_meeting(self, id: int):
        user = get_user(id)
        category = DATABASE.search(user.id, DATABASE.CATEGRY)

        return {
            "id" : id,
            "data" : category
        }

        