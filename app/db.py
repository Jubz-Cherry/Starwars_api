from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker 

DATABASE_URL = "postgresql://postgres:102011@localhost:5432/starwars_api"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
# base para os modelos (tabelas)

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

# SessionLocal é usada para criar sessões (transações) com o banco