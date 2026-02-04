from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from acess.create_access import verify_token
from app.dependencies import get_db
from characters.schema import CharacterResponse
from models import Character, UserFavorite
from .repository import get_character_by_id

router = APIRouter()

@router.get('/allcharacters', response_model=list[CharacterResponse])
def get_all_characters(db: Session = Depends(get_db)):
    characters = db.query(Character).all()
    return characters

@router.get('/curtidos', response_model=list[CharacterResponse])
def get_favorite_characters(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    characters = (
        db.query(Character)
        .join(
            UserFavorite,
            UserFavorite.entity_id == Character.id
        )
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_type == 'character'
        )
        .all()
    )
    if not characters:
        raise HTTPException(
            status_code=404,
            detail='No character favorites yet'
        )

    return characters

@router.post('/{character_id}/favorite')
def favorite_character(
    character_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    # verifica se já curtiu
    already_favorited = (
        db.query(UserFavorite)
        .filter(
            UserFavorite.user_id == user_id,
            UserFavorite.entity_id == character_id,
            UserFavorite.entity_type == 'character'
        )
        .first()
    )

    if already_favorited:
        raise HTTPException(
            status_code=400,
            detail='You already favorited this character'
        )

    favorite = UserFavorite(
        user_id=user_id,
        entity_id=character_id,
        entity_type='character'
    )

    db.add(favorite)
    db.commit()

    return {'message': 'Character favorited'}

@router.delete('/{character_id}/favorite')
def unfavorite_character(
    character_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorite = db.query(UserFavorite).filter_by(
        user_id=user_id,
        entity_id=character_id,
        entity_type='character'
    ).first()

    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(favorite)
    db.commit()

    return {'message': 'Character unfavorited'}
