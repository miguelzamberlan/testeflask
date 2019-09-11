"""App configuration."""
from os import environ
import os


class Config:
    """Set Flask configuration vars from .env file."""

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = True

    # Banco de Dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')