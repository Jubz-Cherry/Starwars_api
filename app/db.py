import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# escolhe qual DB usar
USE_CLOUD = os.getenv("USE_CLOUD", "false").lower() == "true"

if USE_CLOUD:
    DATABASE_URL = os.getenv("DATABASE_URL_CLOUD")
else:
    DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não encontrada no .env")

print("DATABASE_URL:", repr(DATABASE_URL))

engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("ENV", "dev") == "dev"
)

Base = declarative_base()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
