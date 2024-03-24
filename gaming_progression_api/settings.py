from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(override=True)


class Settings(
    BaseSettings,
):
    database_url: str
 

    model_config = SettingsConfigDict(env_file='.env', env_prefix='API_')


@lru_cache
def get_settings() -> Settings:
    return Settings()
