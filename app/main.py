from fastapi import FastAPI
from pydantic_settings import BaseSettings

from app.api.endpoints import portfolio


class Settings(BaseSettings):
    """Application-wide settings pulled from environment variables."""

    IBKR_HOST: str = "localhost"
    IBKR_PORT: int = 5000
    MODE: str = "paper"           # 'paper' or 'live'
    AUTH_TOKEN: str = ""          # leave blank for no-auth testing

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
app = FastAPI()

# Include routers
app.include_router(portfolio.router)


@app.get("/")
async def root():
    return {"status": "ok"}
