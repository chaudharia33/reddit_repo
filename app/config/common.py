import os
from enum import Enum
from pydantic import Field, validator, PostgresDsn
from pydantic_settings import BaseSettings


class SentimentModel(str, Enum):
    TextBOT = "textbot"
    VADER = "vader"

class Settings(BaseSettings):
    project_name="Reddit_API"
    api_main_path: str = '/subfeddit-api'
    feddit_url: str = Field("http://localhost:8080")
    sentiment_model: SentimentModel = Field(SentimentModel.VADER)
    host: str = Field("0.0.0.0")
    port: int = Field(8080)
    reload: bool = Field(True)
    debug: bool = Field(True)
    log_level: str = Field("info")
    access_log: bool = Field(True)
    workers: int = Field(1)

    LOGGING_CONFIG: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "jsonFormatter": {
                "()": "reddit_sentiment_analysis.logs.CustomJsonFormatter",
                "format": "%(levelname)%(asctime)%(location)%(message)",
            },
        },
        "handlers": {
            "consoleHandler": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "jsonFormatter",
            }
        },
        "loggers": {
            "webapp": {
                "handlers": ["consoleHandler"],
                "level": "INFO",
            },
            "uvicorn": {"handlers": ["consoleHandler"]},
            "uvicorn.access": {"handlers": ["consoleHandler"]},
        },
    }

    @validator('api_main_path')
    def validate_api_main_path(cls, v):
        """
        api_main_path has to begin with / and finish without /
        
        Example:
            /subfeddit-api
        """
        if v[0] != '/':
            v = '/' + v
        if v[-1] == '/':
            v = v[:-1]
        return v

    postgres_server: str = os.getenv("postgres_server")
    postgres_user: str = os.getenv("postgres_server")
    postgres_password: str = os.getenv("postgres_server")
    postgres_db: str = os.getenv("postgres_server")
    sqlalchemy_database_uri: str = os.getenv("postgres_server", default= None)

    @validator('sqlalchemy_database_uri', pre=True)
    def assemble_db_connection(cls, v: str, values: dict) -> str:
        """
        Assemble the PostgreSQL database URI with the provided settings.

        Args:
            v (str): The current value of the database URI.
        values (dict): A dictionary containing the settings values.

        Returns:
            str: The assembled PostgreSQL database URI.
        """
        if v is not None:
            return v
        else:
            return PostgresDsn.build(
                            scheme="postgresql",            
                            user=values.get("postgres_user"),
                            password=values.get("postgres_password"),
                            host=values.get("postgres_server"),
                            path=f"/{values.get('postgres_db') or ''}",
                            )
settings = Settings()