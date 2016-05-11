import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = "tnt"
MONGO_DB_IP = "127.0.0.1"
MONGO_DB_PORT = 27017

USERS = {"john": ("john", "pass"),
               "JaneDoe": ("JaneDoe", "Jane"),
               "admin": ("admin", "admin")}
