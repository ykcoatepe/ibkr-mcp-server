from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application-wide settings pulled from environment variables or defaults."""

    IBKR_HOST: str = "localhost"
    IBKR_PORT: int = 5000
    MODE: str = "paper"           # 'paper' or 'live'
    AUTH_TOKEN: str = ""          # leave blank for no-auth testing

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Single global instance imported elsewhere
settings = Settings()