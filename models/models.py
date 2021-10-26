from dataclasses import dataclass
from typing import Optional, List

@dataclass
class User:
    id: float
    email: str
    pw: str
    session_id: Optional[float] = None
    current_category: Optional[str] = None

@dataclass
class Meeting:
    id: float
    pw: str
    time: str
    link: str
    repeating_days: List[str] = []
    name: str = "Meeting"

@dataclass
class Category:
    pass
