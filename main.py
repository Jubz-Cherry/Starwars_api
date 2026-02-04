from dotenv import load_dotenv 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

from fastapi import FastAPI, Depends
import uvicorn  
import os 
from films.routes import router as films_router
from characters.routes import router as characters_routes
from app.dependencies import get_db
from register.routes import router as register_router
from species.routes import router as species_routes
from planets.routes import router as planets_routes
from starships.routes import router as starships_routes

app = FastAPI()

#registram “sub-rotas” organizadas em arquivos separados
app.include_router(register_router, prefix="/auth", tags=["Auth"])
app.include_router(films_router, prefix="/films", tags=["Films"])
app.include_router(characters_routes, prefix="/character", tags=["Character"])
app.include_router(species_routes, prefix="/species", tags=["Species"])
app.include_router(planets_routes, prefix="/planets", tags=["Planets"])
app.include_router(starships_routes, prefix="/starships", tags=["Starships"])

@app.get("/")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)