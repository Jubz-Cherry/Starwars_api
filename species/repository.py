from sqlalchemy.orm import Session
from models import Species

def get_species_by_id(db: Session, species_id: int):
    return db.query(Species).filter(Species.id == species_id).first()