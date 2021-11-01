from pydantic import BaseModel

from dataclasses import dataclass, field
from typing import Optional

class User(BaseModel):
    email: str
    pw: str

@dataclass
class Meeting:
    id: str
    pwd: str
    time: str
    link: str
    category: str
    repeating_days: str
    nickname: str
    meet: str
    name: str = "Meeting"

    def to_dict(self):
        return {
            "id"             : self.id,
            "pwd"            : self.pwd,
            "time"           : self.time,
            "link"           : self.link,
            "category"       : self.link,
            "repeating-days" : self.repeating_days,
            "nickname"       : self.nickname,
            "name"           : self.name
        }

@dataclass
class Category:
    pass
