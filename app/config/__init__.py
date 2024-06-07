import os
from utils.logger import logger
from .common import Settings
from .dev import DevConfig
from .uat import UatConfig
from .prod import ProdConfig

env = "DEV"

def get_settings():
    """Get different settings object according to different values of
    environment variable `MODE`, and use cache to speed up the execution.

    Returns:
        object: The instance of the current used settings class.
    """
    mode_name = os.environ.get(env)
    base_settings = Settings()
    logger.info(base_settings.project_name)
    if mode_name not in {"DEV", "UAT", "PROD"}:
        logger.info("Environement is not defined, default settings are used.")
        return base_settings
    elif mode_name == "DEV":
        return DevConfig()
    elif mode_name == "UAT":
        return UatConfig()
    return ProdConfig()