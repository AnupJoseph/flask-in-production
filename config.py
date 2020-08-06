import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "no-one-will-figure-this-out"

class ProductionConfig(object):
    DEBUG = False

class StagingConfig(object):
    DEBUG = True
    DEVELOPMENT = True

class DevelopmentConfig(object):
    DEBUG = True
    DEVELOPMENT = True

class TestingConfig(object):
    TESTING = True