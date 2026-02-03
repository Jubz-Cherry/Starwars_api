import requests

from app.db import SessionLocal
from models import Species

SWAPI_SPECIES_URL = 'https://swapi.dev/api/species/'


def import_species():
    db = SessionLocal()

    try:
        url = SWAPI_SPECIES_URL

        while url:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for item in data['results']:
                exists = db.query(Species).filter(
                    Species.url == item['url']
                ).first()

                if exists:
                    print(f"Já existe: {item['name']}")
                    continue

                species = Species(
                    name=item['name'],
                    classification=item['classification'],
                    designation=item['designation'],
                    average_height=item['average_height'],
                    skin_colors=item['skin_colors'],
                    hair_colors=item['hair_colors'],
                    eye_colors=item['eye_colors'],
                    average_lifespan=item['average_lifespan'],
                    language=item['language'],
                    homeworld_url=item['homeworld'],
                    people=item['people'],
                    films=item['films'],
                    url=item['url'],
                )

                db.add(species)
                print(f"Espécie adicionada: {item['name']}")

            db.commit()
            url = data['next']

        print('Importação de species finalizada')

    finally:
        db.close()


if __name__ == '__main__':
    import_species()
