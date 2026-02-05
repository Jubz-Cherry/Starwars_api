import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = None

USE_CLOUD = os.getenv("USE_CLOUD", "false").lower() == "true"

if USE_CLOUD:
    # Configuração para Cloud SQL via Unix socket
    DB_NAME = "starwars-db"               # nome exato do banco
    DB_USER = "postgres"                  # usuário do banco
    DB_PASS = "Postgres10201191%21"      # senha já percent-encoded
    DB_HOST = "/cloudsql/deep-burner-486320-d9:southamerica-east1:starwars-post"  # Unix socket do Cloud SQL

    # URL de conexão para SQLAlchemy usando Unix socket
    DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@/{DB_NAME}?host={DB_HOST}"

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
