"""
    config.py
    - settings for the flask application object
"""
import os


class BaseConfig():
    """"
    Base configuration class for storing configs.
    """
    # postgres conf
    # these values should be modified prior to using
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'testusr')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'testdb')
    POSTGRES_HOST = 'postgres'
    default_postgres_uri = "postgresql+psycopg2://{}:{}@{}:5432/{}".format(
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        POSTGRES_HOST,
        POSTGRES_DB
    )
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', default_postgres_uri)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BROKER = "mqtt"
    # lets keep it simple with default port
    PORT = 1883
    TIMELIVE = 120

