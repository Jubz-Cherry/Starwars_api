import requests
from app.db import SessionLocal
from models import Film, Character, FilmCharacter

db = SessionLocal()

SWAPI_FILMS = "https://swapi.dev/api/films/"
SWAPI_PEOPLE = "https://swapi.dev/api/people/"

def seed_films():
    response = requests.get(SWAPI_FILMS).json()

    for film in response["results"]:
        exists = db.query(Film).filter(Film.url == film["url"]).first()
        if exists:
            continue

        new_film = Film(
            title=film["title"],
            episode=film["episode_id"],
            release_date=film["release_date"],
            director=film["director"],
            producer=film["producer"],
            synopsis=film["opening_crawl"],
            url=film["url"]
        )

        db.add(new_film)

    db.commit()

def seed_characters_and_relations():
    response = requests.get(SWAPI_PEOPLE).json()

    for person in response["results"]:
        character = db.query(Character).filter(Character.url == person["url"]).first()

        if not character:
            character = Character(
                name=person["name"],
                gender=person["gender"],
                birth_year=person["birth_year"],
                height=person["height"],
                mass=person["mass"],
                homeworld_url=person["homeworld"],
                url=person["url"]
            )
            db.add(character)
            db.commit()
            db.refresh(character)

        for film_url in person["films"]:
            film = db.query(Film).filter(Film.url == film_url).first()
            if film:
                relation_exists = (
                    db.query(FilmCharacter)
                    .filter(
                        FilmCharacter.film_id == film.id,
                        FilmCharacter.character_id == character.id
                    )
                    .first()
                )

                if not relation_exists:
                    db.add(
                        FilmCharacter(
                            film_id=film.id,
                            character_id=character.id
                        )
                    )

    db.commit()

if __name__ == "__main__":
    seed_films()
    seed_characters_and_relations()
    print("Banco populado com sucesso")
