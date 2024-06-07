from .common import Settings


class DevConfig(Settings):
    debug = True
    access_log: bool = True
    workers: int = 1
    sentiment_model= "textbot"
