from pydantic import BaseModel
from typing import List

class NoteSection(BaseModel):
    title: str
    bullets: List[str]
