from sqlalchemy.orm import Session
from models import Character

def get_character_by_id(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()