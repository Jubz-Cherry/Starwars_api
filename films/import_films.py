import requests
from datetime import datetime

from app.db import SessionLocal
from models import Film

SWAPI_FILMS_URL = 'https://swapi.dev/api/films/'

def import_films():
    response = requests.get(SWAPI_FILMS_URL)
    response.raise_for_status()

    data = response.json()
    films = data['results']

    db = SessionLocal()

    try:
        for film in films:
            # evita duplicar
            exists = db.query(Film).filter(
                Film.episode == film['episode_id']
            ).first()

            if exists:
                print(f" Filme já existe: Episódio {film['episode_id']}")
                continue

            new_film = Film(
                title=film['title'],
                episode=film['episode_id'],
                release_date=datetime.strptime(
                    film['release_date'], '%Y-%m-%d'
                ).date(),
                director=film['director'],
                producer=film['producer'],
                synopsis=film['opening_crawl'],
                url=film['url']
            )

            db.add(new_film)
            print(f"Filme adicionado: {film['title']}")

        db.commit()
        print('Importação finalizada')

    finally:
        db.close()

if __name__ == '__main__':
    import_films()
