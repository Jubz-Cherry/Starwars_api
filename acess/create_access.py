import os
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from app.dependencies import get_db
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

# 3️⃣ agora sim ler as variáveis
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
SECRET_KEY = os.getenv('SECRET_KEY')
ACCES_TOKEN_EXPIRED_MINUTE = int(
    os.getenv('ACCES_TOKEN_EXPIRED_MINUTE', 30)
)

# 4️⃣ falhar logo se der ruim
if not SECRET_KEY:
    raise RuntimeError('SECRET_KEY não foi carregada do .env')


def criar_token(id_usuario: int):
    data_expiracao = datetime.now(timezone.utc) + timedelta(
        minutes=ACCES_TOKEN_EXPIRED_MINUTE
    )

    payload = {
        'sub': str(id_usuario),
        'exp': data_expiracao,
        'iat': datetime.now(timezone.utc)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> int:
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get('sub')
        if not user_id:
            raise HTTPException(status_code=401)

        return int(user_id)

    except JWTError:
        raise HTTPException(status_code=401)