import requests

from app.db import SessionLocal
from models import Character

SWAPI_PEOPLE_URL = 'https://swapi.dev/api/people/'


def import_characters():
    db = SessionLocal()

    try:
        url = SWAPI_PEOPLE_URL

        while url:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for person in data['results']:
                exists = db.query(Character).filter(
                    Character.url == person['url']
                ).first()

                if exists:
                    print(f" Já existe: {person['name']}")
                    continue

                character = Character(
                    name=person['name'],
                    gender=person['gender'],
                    birth_year=person['birth_year'],
                    height=person['height'],
                    mass=person['mass'],
                    homeworld_url=person['homeworld'],
                    films=person['films'],        
                    species=person['species'], 
                    films_count=len(person['films']),
                    url=person['url'],
                )

                db.add(character)
                print(f"Personagem adicionado: {person['name']}")

            db.commit()
            url = data['next']

        print('Importação finalizada')

    finally:
        db.close()


if __name__ == '__main__':
    import_characters()
