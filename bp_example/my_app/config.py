class Config:
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    SERVER_NAME = "0.0.0.0"
    PORT = 4444
    SECRET_KEY = "0748996daa60a86f9bc6c66501a54f984ba6792401fe4f28f00b0f54b492be9c"


class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = "0.0.0.0"
    PORT = 3333
