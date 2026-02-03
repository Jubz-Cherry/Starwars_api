from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from acess.create_access import verify_token
from models import UserFavorite
from .repository import get_film_by_id
from .schema import FilmSchema
from app.dependencies import get_db

router = APIRouter(prefix="/films", tags=["Films"])

@router.get("/", response_model=FilmSchema)
def get_film(
    film_id: int,
    db: Session = Depends(get_db)
):
    film = get_film_by_id(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@router.get('/curtidos', response_model=list[FilmSchema])
def get_favorites(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorites = (
        db.query(UserFavorite)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_type == 'film'
        )
        .all()
    )
    
    if not favorites:
        raise HTTPException(
            status_code=404,
            detail='No film favorites yet'
        )

    film_ids = [f.entity_id for f in favorites]

    return [get_film_by_id(db, film_id) for film_id in film_ids]

@router.post('/{film_id}/favorite')
def favorite_film(
    film_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    already_favorited = (
        db.query(UserFavorite)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_id == film_id,
            UserFavorite.entity_type == 'film'
        )
        .first()
    )

    if already_favorited:
        raise HTTPException(
            status_code=400,
            detail='You already favorited this film'
        )

    favorite = UserFavorite(
        user_id=user_id,
        entity_id=film_id,
        entity_type='film'
    )

    db.add(favorite)
    db.commit()

    return {'message': 'Film favorited'}

@router.delete('/{film_id}/favorite')
def unfavorite_film(
    film_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorite = db.query(UserFavorite).filter_by(
        user_id=user_id,
        entity_id=film_id
    ).first()

    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(favorite)
    db.commit()

    return {'message': 'Film unfavorited'}
