import requests

from app.db import SessionLocal
from models import Planet

SWAPI_PLANETS_URL = 'https://swapi.dev/api/planets/'


def import_planets():
    db = SessionLocal()

    try:
        url = SWAPI_PLANETS_URL

        while url:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for planet_data in data['results']:
                # evita duplicar planeta
                exists = (
                    db.query(Planet)
                    .filter(Planet.url == planet_data['url'])
                    .first()
                )

                if exists:
                    print(f"Já existe: {planet_data['name']}")
                    continue

                planet = Planet(
                    name=planet_data['name'],
                    rotation_period=planet_data['rotation_period'],
                    orbital_period=planet_data['orbital_period'],
                    diameter=planet_data['diameter'],
                    climate=planet_data['climate'],
                    gravity=planet_data['gravity'],
                    terrain=planet_data['terrain'],
                    surface_water=planet_data['surface_water'],
                    population=planet_data['population'],

                    # listas (JSON)
                    residents=planet_data['residents'],  # pessoas
                    films=planet_data['films'],

                    url=planet_data['url']
                )

                db.add(planet)
                print(f"Planeta adicionado: {planet_data['name']}")

            db.commit()
            url = data['next']

        print('Importação de planetas finalizada')

    finally:
        db.close()


if __name__ == '__main__':
    import_planets()
