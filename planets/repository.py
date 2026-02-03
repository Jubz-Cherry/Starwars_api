from sqlalchemy.orm import Session
from models import Planet

def get_planet_by_id(db: Session, planet_id: int):
    return db.query(Planet).filter(Planet.id == planet_id).first()