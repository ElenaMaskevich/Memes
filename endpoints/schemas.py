from pydantic import BaseModel
from typing import Any


class CreateMeme(BaseModel):
    text: str
    url: str
    tags: list
    info: dict[str, Any]


class PutMeme(BaseModel):
    id: int
    text: str
    url: str
    tags: list
    info: dict[str, Any]
