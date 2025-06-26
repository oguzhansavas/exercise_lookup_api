# app/models.py
from typing import List
from pydantic import BaseModel

class Exercise(BaseModel):
    id: int
    name: str
    muscle: str
    equipment: List[str]
    difficulty: str
