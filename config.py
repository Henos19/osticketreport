import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'development')
    MYSQL_DB = os.environ.get('MYSQL_DB')
    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}@localhost:{MYSQL_PORT}/{MYSQL_DB}"

    # SQLALCHEMY_TRACK_MODIFICATIONS = False