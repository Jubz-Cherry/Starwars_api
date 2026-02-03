from pydantic import BaseModel
from typing import List, Optional

class PlanetResponse(BaseModel):
    id: int
    name: str
    rotation_period: Optional[str]
    orbital_period: Optional[str]
    diameter: Optional[str]
    climate: Optional[str]
    gravity: Optional[str]
    terrain: Optional[str]
    surface_water: Optional[str]
    population: Optional[str]
    residents: List[str]
    films: List[str]
    url: str

    class Config:
        from_attributes = True