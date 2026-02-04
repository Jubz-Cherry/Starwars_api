from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from acess.create_access import verify_token
from app import db
from app.dependencies import get_db
from species.schema import SpeciesResponse
from models import Species, UserFavorite
from .repository import get_species_by_id

router = APIRouter()

@router.get('/allspecies', response_model=list[SpeciesResponse])
def get_all_species(db: Session = Depends(get_db)):
    species = db.query(Species).all()
    return species

@router.get('/favorites', response_model=list[SpeciesResponse])
def get_favorites(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorites = (
        db.query(Species)
        .join(UserFavorite, UserFavorite.entity_id == Species.id)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_type == 'species'
        )
        .all()
    )

    if not favorites:
        raise HTTPException(
            status_code=404,
            detail='No species favorites yet'
        )

    return favorites

@router.post('/{species_id}/favorite')
def favorite_species(
    species_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    # verifica se já curtiu
    already_favorited = (
        db.query(UserFavorite)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_id == species_id,
            UserFavorite.entity_type == 'species'
        )
        .first()
    )

    if already_favorited:
        raise HTTPException(
            status_code=400,
            detail='You already favorited this species'
        )

    favorite = UserFavorite(
        user_id=user_id,
        entity_id=species_id,
        entity_type='species'
    )

    db.add(favorite)
    db.commit()

    return {'message': 'Species favorited'}

@router.delete('/{species_id}/favorite')
def unfavorite_species(
    species_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorite = db.query(UserFavorite).filter_by(
        user_id=user_id,
        entity_id=species_id,
        entity_type='species'
    ).first()

    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(favorite)
    db.commit()

    return {'message': 'Species unfavorited'}
