from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator, PostgresDsn


class Settings(BaseSettings):
    PROJECT_NAME: str
    ALLOWED_ORIGINS: List[AnyHttpUrl] = []
    DATABASE_URL: PostgresDsn

    @validator("ALLOWED_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
