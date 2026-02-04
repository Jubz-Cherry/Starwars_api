from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from acess.create_access import verify_token
from app.dependencies import get_db
from planets.schema import PlanetResponse
from models import Planet, UserFavorite
from .repository import get_planet_by_id

router = APIRouter()

@router.get('/allplanets', response_model=list[PlanetResponse])
def get_all_planets(db: Session = Depends(get_db)):
    planets = db.query(Planet).all()
    return planets

@router.get('/favorites', response_model=list[PlanetResponse])
def get_favorites(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorites = (
        db.query(Planet)
        .join(UserFavorite, UserFavorite.entity_id == Planet.id)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_type == 'planet'
        )
        .all()
    )

    if not favorites:
        raise HTTPException(
            status_code=404,
            detail='No planet favorites yet'
        )

    return favorites

@router.post('/{planets_id}/favorite')
def favorite_planet(
    planet_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    # verifica se já curtiu
    already_favorited = (
        db.query(Planet)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_id == planet_id,
            UserFavorite.entity_type == 'planet'
        )
        .first()
    )

    if already_favorited:
        raise HTTPException(
            status_code=400,
            detail='You already favorited this planet'
        )

    favorite = UserFavorite(
        user_id=user_id,
        entity_id=planet_id,
        entity_type='planet'
    )

    db.add(favorite)
    db.commit()

    return {'message': 'Planet favorited'}

@router.delete('/{planet_id}/favorite')
def unfavorite_planet(
    planet_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorite = db.query(UserFavorite).filter_by(
        user_id=user_id,
        entity_id=planet_id,
        entity_type='planet'
    ).first()

    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(favorite)
    db.commit()

    return {'message': 'Planet unfavorited'}
