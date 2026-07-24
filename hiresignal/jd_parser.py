
from pydantic import BaseModel
from typing import List


class JDOutput(BaseModel):
    required_skills: List[str]
    nice_to_have: List[str]
    years_exp: int
    seniority: str
