from pydantic import BaseSettings

class Settings(BaseSettings):
    current_datetime: str
    current_user_login: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings(
    current_datetime='2026-02-23 20:04:40',
    current_user_login='CrowDeAd66'
)