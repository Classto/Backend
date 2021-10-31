from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException

from models import Meeting
from app import SESSION, DATABASE

import json

meeting_router = InferringRouter()

# 미팅업데이트
# 카테고리업데이트
# 미팅가져오기
# 카테고리가져오기

def get_user(id):
    session = SESSION.find(id)
    if session == ():
        raise HTTPException(404, detail="user not found")

    user = DATABASE.info(session[0])
    user["expir_time"] = session[1]

    return user

@cbv(meeting_router)
class Meeting:
    @meeting_router.get("/schedule/{id}")
    async def get_meeting(self, id: int):
        user = get_user(id)
        schedule = DATABASE.search(user["id"], DATABASE.SCHEDULE)

        return {
            "id" : id,
            "data" : schedule
        }

    @meeting_router.get("/category/{id}")
    async def get_category(self, id: int):
        user = get_user(id)
        category = DATABASE.search(user["id"], DATABASE.CATEGRY)

        return {
            "id" : id,
            "data" : category
        }
    
    @meeting_router.post("/schedule/{id}")
    async def edit_schedule(self, id: int, meeting: Meeting):
        user = get_user(id)
        category = meeting.category

        schedule = DATABASE.search(user["id"], DATABASE.SCHEDULE)
        print(schedule)
        schedule[category].append(meeting.to_dict())
        DATABASE.edit(user["id"], DATABASE.SCHEDULE, schedule)

        return {
            "id" : id,
            "schedule" : schedule[category]
        }

    @meeting_router.post("/category/{id}")
    async def edit_category(self, id: int, new_category: str):
        user = get_user(id)

        category = DATABASE.search(user["id"], DATABASE.CATEGRY)
        category.append(new_category)
        DATABASE.edit(user["id"], DATABASE.CATEGRY, category)

        schedule = DATABASE.search(user["id"], DATABASE.SCHEDULE)
        schedule[new_category] = []
        DATABASE.edit(user["id"], DATABASE.SCHEDULE, schedule)

        return {
            "id" : id,
            "category" : category
        }
