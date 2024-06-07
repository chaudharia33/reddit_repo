from .common import Settings


class ProdConfig(Settings):
    debug = False
    access_log: bool = False
    workers: int = 3
    sentiment_model= "textbot"