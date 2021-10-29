from pydantic import BaseModel

from dataclasses import dataclass, field
from typing import Optional

class User(BaseModel):
    email: str
    pw: str

@dataclass
class Meeting:
    id: float
    pw: str
    time: str
    link: str
    repeating_days: field(default_factory=list)
    name: str = "Meeting"

@dataclass
class Category:
    pass
