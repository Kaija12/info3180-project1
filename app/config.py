import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SCRAM-SHA-256$4096:ZzfMZquE7FpRRKrkwS0Beg==$0qnbqynRwXWQ3yp7y+9p+OgJ9dLYvILfvZ/cqZ3xKPQ=:xapqaJFFPY/Epid4k+ZqEw13Mh6EyveMPY9dAWw5lxw=')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:kaija@localhost/info3180-project1'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/uploads')