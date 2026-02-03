from passlib.context import CryptContext

argon2_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)