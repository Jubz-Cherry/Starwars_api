from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

from fastapi import FastAPI, Depends
import uvicorn
from films.routes import router as films_router
from characters.routes import router as characters_routes
from app.dependencies import get_db
from register.routes import router as register_router
from species.routes import router as species_routes
from planets.routes import router as planets_routes
from starships.routes import router as starships_routes

app = FastAPI()

#registram “sub-rotas” organizadas em arquivos separados
app.include_router(register_router)
app.include_router(films_router)
app.include_router(characters_routes)
app.include_router(species_routes)
app.include_router(planets_routes)
app.include_router(starships_routes)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
    