from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class StarshipResponse(BaseModel):
    id: int
    name: str
    model: Optional[str]
    manufacturer: Optional[str]
    length: Optional[str]
    max_atmosphering_speed: Optional[str]
    crew: Optional[str]
    passengers: Optional[str]
    cargo_capacity: Optional[str]
    consumables: Optional[str]
    hyperdrive_rating: Optional[str]
    MGLT: Optional[str]
    starship_class: Optional[str]

    films: List[str]

    url: str

    model_config = ConfigDict(from_attributes=True)
