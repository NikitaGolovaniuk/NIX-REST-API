class BaseConfig:
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@db:5432/my_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://test:test@db/my_test_db"
    TESTING = True
    DEBUG = True
    ENV = "testing"
