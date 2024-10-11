from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    START_DELAY: list[int] = [1, 30]
    SLEEP_TIME: list[int] = [1*60*60, 3*60*60]
    FORTUNE_REWARDS: list[int] = [200, 250, 500, 750, 1000, 1250, 1500, 2000]
    AUTO_TASK: bool = True
    JOIN_CHANNELS: bool = True

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
