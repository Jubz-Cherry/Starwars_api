from app.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Cria a sessão no banco, depois a "entrega" para a rota q precisa dela
# e fecha a sessão quando a rota termina
