"""Application settings using Pydantic Settings."""
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    ########################
    # Server Configuration #
    ########################

    # Server
    host: str = "0.0.0.0"
    port: int = 8080
    log_level: str = "INFO"

    #########################
    # ApiKeys Configuration #
    #########################

    # API Keys
    google_api_key: str = ""
   
    # Gemini LLM
    gemini_model: str = "gemini-2.5-flash-native-audio-preview-12-2025"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()