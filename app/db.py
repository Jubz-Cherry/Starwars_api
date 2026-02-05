import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = None

USE_CLOUD = os.getenv("USE_CLOUD", "false").lower() == "true"

if USE_CLOUD:
    # nome exato do banco
    DB_NAME = "starwars-db"
    DATABASE_URL = f"postgresql+psycopg://postgres:Postgres10201191%21@/{DB_NAME}?host=/cloudsql/deep-burner-486320-d9:southamerica-east1:starwars-post"

else:
    DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")

engine = None
SessionLocal = None

if DATABASE_URL:
    engine = create_engine(
        DATABASE_URL,
        echo=os.getenv("ENV", "dev") == "dev"
    )

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

Base = declarative_base()
