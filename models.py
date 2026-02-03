from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db import Base

class Film(Base):
    __tablename__= "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    episode = Column(Integer)
    release_date = Column(Date)
    director = Column(String)
    producer = Column(String)
    synopsis = Column(Text)
    url= Column(String)

class Users(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

class UserFavorite(Base):
    __tablename__ = 'user_favorites'

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )

    entity_type = Column(String, nullable=False)  # 'character', 'species', 'planet', 'starship', 'film'
    entity_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('Users')

class Character(Base):
    __tablename__ = 'characterr'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String)
    birth_year = Column(String)
    height = Column(String)
    mass = Column(String)

    homeworld_url = Column(String)
    url = Column(String, unique=True)

    films_count = Column(Integer)

    films = Column(JSON, nullable=False, default=list)
    species = Column(JSON, nullable=False, default=list)

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    skin_colors = Column(String)
    hair_colors = Column(String)
    eye_colors = Column(String)
    average_lifespan = Column(String)
    language = Column(String)

    homeworld_url = Column(String)
    people = Column(JSON, nullable=False, default=list)
    films = Column(JSON, nullable=False, default=list)

    url = Column(String, unique=True)

class Planet(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rotation_period = Column(String, nullable=True)
    orbital_period = Column(String, nullable=True)
    diameter = Column(String, nullable=True)
    climate = Column(String, nullable=True)
    gravity = Column(String, nullable=True)
    terrain = Column(String, nullable=True)
    surface_water = Column(String, nullable=True)
    population = Column(String, nullable=True)

    residents = Column(JSON, nullable=False, default=list)
    films = Column(JSON, nullable=False, default=list)

    url = Column(String, unique=True, nullable=False)
    url = Column(String, unique=True, nullable=False)

class Starship(Base):
    __tablename__ = 'starships'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=True)
    manufacturer = Column(String, nullable=True)
    length = Column(String, nullable=True)
    max_atmosphering_speed = Column(String, nullable=True)
    crew = Column(String, nullable=True)
    passengers = Column(String, nullable=True)
    cargo_capacity = Column(String, nullable=True)
    consumables = Column(String, nullable=True)
    hyperdrive_rating = Column(String, nullable=True)
    MGLT = Column(String, nullable=True)
    starship_class = Column(String, nullable=True)

    films = Column(JSON, nullable=False, default=list)

    url = Column(String, unique=True, nullable=False)