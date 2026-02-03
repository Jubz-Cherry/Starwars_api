from datetime import date
from pydantic import BaseModel

class FilmSchema(BaseModel):
    id: int
    title: str
    episode: int
    release_date: date
    synopsis: str
    