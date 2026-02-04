Star Wars API

Uma API REST construída em Python usando FastAPI, inspirada no universo de Star Wars. O projeto fornece endpoints organizados para consulta de dados como filmes, personagens, planetas, espécies e naves, com autenticação, testes automatizados e controle de versionamento de banco de dados.
O projeto foi pensado como uma API organizada, escalável e completa, seguindo boas práticas de separação de camadas, validação de dados, autenticação e testes automatizados.

- Tecnologias usadas:
- Linguagem
Python

- Framework Web
FastAPI – framework moderno, rápido e tipado para APIs
Uvicorn – servidor ASGI

- Banco de Dados
PostgreSQL
SQLAlchemy – ORM
Alembic – controle de migrations
psycopg – driver PostgreSQL

- Validação e Tipagem
Pydantic – validação e serialização de dados
typing – tipagem estática

- Segurança
python-jose – JWT (JSON Web Tokens)
argon2 – hash seguro de senhas

- Comunicação HTTP
httpx – cliente HTTP assíncrono

- Configuração
python-dotenv – gerenciamento de variáveis de ambiente

- Testes
pytest – testes unitários

- Estrutura do Projeto:

Starwars_api/
    ├── alembic/
    │   ├── versions/
    │   └── env.py
    ├── films/
    |   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    │   └── schema.py
    ├── characters/
    ├── planets/
    ├── species/
    ├── starships/
    ├── register/
    |   ├── __init__.py
    |   ├── repository.py
    │   ├── routes.py
    │   └── schema.py
    ├── acess/
    │   ├── create_acess.py
    │   └── schema.py
    ├── tests/
    │   └── test_main.py
    ├── main.py
    ├── models.py
    ├── requirements.txt
    └── README.md

- Como Executar o Projeto
.1 Clonar o Repositório:
  git clone https://github.com/seu-usuario/Starwars_api.git
  cd Starwars_api

.2 Criar e Ativar o Ambiente Virtual
  python -m venv venv
  
  # Windows
  venv\Scripts\activate

  # Linux / macOS
  source venv/bin/activate

.3 Instalar as Dependências
  pip install -r requirements.txt

.4 Configurar Variáveis de Ambiente
  Crie um arquivo .env na raiz do projeto:
  
  DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/starwars
  SECRET_KEY=sua_chave_secreta
  ALGORITHM=HS256
  ACCESS_TOKEN_EXPIRE_MINUTES=30

.5 Banco de Dados e Migrations:
  Criar as Tabelas:
  alembic upgrade head

.6 Criar uma Nova Migration:
  alembic revision --autogenerate -m "descricao"

- Rodando a API:
  uvicorn app.main:app --reload

- A API ficará disponível em:
  http://127.0.0.1:8000

- Documentação Automática:
  FastAPI gera documentação automaticamente:
    Swagger UI:
    http://127.0.0.1:8000/docs

    ReDoc:
    http://127.0.0.1:8000/redoc
  
Essas páginas listam todas as rotas disponíveis, parâmetros, schemas e respostas.

- Autenticação:
  A API utiliza JWT (JSON Web Token):
    Login gera um token
    O token deve ser enviado no header:
    Authorization: Bearer <token>

Rotas protegidas exigem autenticação válida.

- Testes Automatizados:
  Os testes são feitos com pytest.
  Executar os testes:
  python -m pytest

  Exemplo de saída esperada:
  23 passed in 2.58s
Isso indica que todas as rotas e comportamentos testados estão funcionando corretamente.

- Sobre os Testes Unitários
  Os testes atuais validam:
  
- Inicialização da aplicação

- Respostas HTTP das rotas

- Status codes

O uso de pytest garante uma boa base de confiabilidade do projeto.

- Considerações Finais:

Este projeto foi desenvolvido com foco em aprendizado, organização e boas práticas. Ele pode ser facilmente expandido com novos recursos, endpoints ou integrações.



