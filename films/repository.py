from sqlalchemy.orm import Session
from models import Film

def get_film_by_id(db: Session, film_id: int):
    return db.query(Film).filter(Film.id == film_id).first()
