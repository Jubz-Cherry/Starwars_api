from fastapi import APIRouter, Depends, HTTPException
from requests import Session

from acess.create_access import verify_token
from app.dependencies import get_db
from models import UserFavorite
from starships.schema import StarshipResponse
from models import Starship
from .repository import get_starship_by_id

router = APIRouter()

@router.get('/allstarships', response_model=list[StarshipResponse])
def get_all_starships(db: Session = Depends(get_db)):
    starships = db.query(Starship).all()
    return starships

@router.get('/favorites', response_model=list[StarshipResponse])
def get_favorites(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorites = (
        db.query(Starship)
        .join(UserFavorite, UserFavorite.entity_id == Starship.id)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_type == 'starship'
        )
        .all()
    )

    if not favorites:
        raise HTTPException(
            status_code=404,
            detail='No starships favorites yet'
        )

    return favorites

@router.post('/{starship_id}/favorite')
def favorite_starship(
    starship_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    # verifica se já curtiu
    already_favorited = (
        db.query(UserFavorite)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_id == starship_id,
            UserFavorite.entity_type == 'starship'
        )
        .first()
    )

    if already_favorited:
        raise HTTPException(
            status_code=400,
            detail='You already favorited this starship'
        )

    favorite = UserFavorite(
        user_id=user_id,
        entity_id=starship_id,
        entity_type='starship'
    )

    db.add(favorite)
    db.commit()

    return {'message': 'Starship favorited'}

@router.delete('/{starship_id}/favorite')
def unfavorite_starship(
    starship_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorite = db.query(UserFavorite).filter_by(
        user_id=user_id,
        entity_id=starship_id,
        entity_type='starship'
    ).first()

    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(favorite)
    db.commit()

    return {'message': 'Starship unfavorited'}
