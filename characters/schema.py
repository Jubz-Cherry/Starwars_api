from typing import List
from pydantic import BaseModel, ConfigDict

class CharactersSchema(BaseModel):
    id: int
    name: str
    species: str
    gender: str
    films: List[int]


class CharacterResponse(BaseModel):
    id: int
    name: str
    gender: str | None
    birth_year: str | None
    height: str | None
    mass: str | None
    homeworld_url: str | None
    films_count: int
    films: List[str]
    species: List[str]

    model_config = ConfigDict(from_attributes=True)