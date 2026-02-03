import requests

from app.db import SessionLocal
from models import Starship

SWAPI_STARSHIPS_URL = 'https://swapi.dev/api/starships/'


def import_starships():
    db = SessionLocal()

    try:
        url = SWAPI_STARSHIPS_URL

        while url:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for item in data['results']:
                exists = db.query(Starship).filter(
                    Starship.url == item['url']
                ).first()

                if exists:
                    print(f"Já existe: {item['name']}")
                    continue

                starship = Starship(
                    name=item['name'],
                    model=item['model'],
                    manufacturer=item['manufacturer'],
                    length=item['length'],
                    max_atmosphering_speed=item['max_atmosphering_speed'],
                    crew=item['crew'],
                    passengers=item['passengers'],
                    cargo_capacity=item['cargo_capacity'],
                    consumables=item['consumables'],
                    hyperdrive_rating=item.get('hyperdrive_rating'),
                    MGLT=item.get('MGLT'),
                    starship_class=item['starship_class'],
                    films=item['films'],
                    url=item['url'],
                )

                db.add(starship)
                print(f"Starship adicionada: {item['name']}")

            db.commit()
            url = data['next']

        print('Importação de starships finalizada')

    finally:
        db.close()

if __name__ == '__main__':
    import_starships()
