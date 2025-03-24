from typing import List

from pydantic import BaseModel


class TourRequest(BaseModel):
    name: str
    job: str
    age: int
    hobbies: List[str]


class PuzzleRequest(BaseModel):
    location: str
    location_info: str
    user_interests: List[str]
    user_job: str
    location_story: str

class HintRequest(BaseModel):
    location: str
    question: str
    answer: str
    hint_level: int

class ExtraInfo(BaseModel):
    title: str