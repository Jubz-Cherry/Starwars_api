from sqlalchemy.orm import Session
from models import Starship

def get_starship_by_id(db: Session, starship_id: int):
    return db.query(Starship).filter(Starship.id == starship_id).first()