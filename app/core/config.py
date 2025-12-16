from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://usuario:123456@localhost:3309/edu-cart"

    # JWT Authentication
    SECRET_KEY: str = "09d25e09f5"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

settings = Settings()
