import os

DEBUG = True
SECRET_KET = os.environ["SECRET_KEY"]
SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
