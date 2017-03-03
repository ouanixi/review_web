import os

SECRET_KEY = "oijfdoijsaoifjaosijdoija"
DEBUG = True
DB_NAME = "name"
DB_USER = "name"
DB_PASS = "pass"
DB_SERVICE = "service"
DB_PORT = "port"
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)