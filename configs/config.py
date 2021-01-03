from transport.sanic.config import SanicConfig


class AppConfig:
    sanic: SanicConfig

    def __init__(self):
        self.sanic = SanicConfig()
