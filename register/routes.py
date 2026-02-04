from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from characters.repository import get_character_by_id
from films.repository import get_film_by_id
from species.repository import get_species_by_id
from planets.repository import get_planet_by_id
from starships.repository import get_starship_by_id
from models import Film, Film, UserFavorite
from .repository import create_user, login_user, show_users, change_user, delete_user_by_id
from .schema import UserSchema, LoginSchema, UserResponseSchema, UserUpdateSchema
from app.dependencies import get_db
from acess.schema import TokenSchema 
from acess.create_access import criar_token, verify_token 

router = APIRouter()

@router.post("/register", response_model= UserSchema)
def register_user(
    user_create: UserSchema, 
    db: Session = Depends(get_db)
    ):
    return create_user(db, user_create)

@router.post("/login", response_model=TokenSchema)
def login(
    user_login: LoginSchema,
    db: Session = Depends(get_db)
    ):
    user = login_user(db, user_login)

    access_token = criar_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get('/allusers')
def all_users(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    print(user_id)  # agora você SABE quem chamou
    return show_users(db)

@router.delete("/users/{user_id}", response_model=UserResponseSchema)
def delete_user(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    print(f'User ID:{user_id} requested deletion of their account.')
    return delete_user_by_id(db, user_id)

@router.put("/users/{user_id}", response_model=UserResponseSchema)
def update_user(
    user_data: UserUpdateSchema,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    return change_user(db, user_id, user_data)

@router.get('/me/favorites')
def my_favorites(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    favorites = (
        db.query(UserFavorite)
        .filter(UserFavorite.user_id == user_id)
        .all()
    )

    if not favorites:
        return {'message': 'No favorites yet'}

    result = {
        'films': [],
        'characters': [],
        'planets': [],
        'species': [],
        'starships': []
    }

    for fav in favorites:
        if fav.entity_type == 'film':
            result['films'].append(get_film_by_id(db, fav.entity_id))

        elif fav.entity_type == 'character':
            result['characters'].append(get_character_by_id(db, fav.entity_id))

        elif fav.entity_type == 'planet':
            result['planets'].append(get_planet_by_id(db, fav.entity_id))

        elif fav.entity_type == 'species':
            result['species'].append(get_species_by_id(db, fav.entity_id))

        elif fav.entity_type == 'starship':
            result['starships'].append(get_starship_by_id(db, fav.entity_id))

    return result
