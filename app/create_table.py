from app.db import engine, Base
from models import Film, Users, UserFavorite  # importa todos os modelos que foram criados


# Cria todas as tabelas definidas em Base
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")


