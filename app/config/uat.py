from .common import Settings


class UatConfig(Settings):
    debug = True
    access_log: bool = True
    workers: int = 1
    sentiment_model= "textbot"