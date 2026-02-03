from sqlalchemy.orm import Session
from models import Users
from .schema import UserSchema, LoginSchema, UserUpdateSchema
from fastapi import HTTPException, status
from core.security import argon2_context


def create_user(db: Session, user_data: UserSchema):
    existing_user = (
        db.query(Users)
        .filter(Users.email == user_data.email)
        .first()
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered!"
    )
    user = Users(
        name=user_data.name,
        email=user_data.email,
        password= argon2_context.hash(user_data.password)

    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(db: Session, login_data: LoginSchema):
    user = (
        db.query(Users)
        .filter(Users.email == login_data.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )

    password_valid = argon2_context.verify(
        login_data.password,
        user.password
    )

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha incorreta"
        )

    return user

def show_users(db: Session):
    return db.query(Users).all()

def delete_user_by_id(db: Session, user_id: int):
    user = db.query(Users).filter(Users.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()
    return user

def change_user(db: Session, user_id: int, change_data: UserUpdateSchema):
    user = db.query(Users).filter(Users.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if change_data.name is not None:
        user.name = change_data.name

    if change_data.email is not None:
        user.email = change_data.email

    if change_data.password is not None:
        user.password = argon2_context.hash(change_data.password)

    db.commit()
    db.refresh(user)
    return user
