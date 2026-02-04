from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class SpeciesResponse(BaseModel):
    id: int
    name: str
    classification: Optional[str]
    designation: Optional[str]
    average_height: Optional[str]
    skin_colors: Optional[str]
    hair_colors: Optional[str]
    eye_colors: Optional[str]
    average_lifespan: Optional[str]
    language: Optional[str]

    homeworld_url: Optional[str]
    people: List[str]
    films: List[str]
    url: str

    model_config = ConfigDict(from_attributes=True)