import os


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    # shoplytics
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}