import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', "root"),
    os.getenv('DB_PASSWORD', "cacapa"),
    os.getenv('DB_HOST', "localhost"),
    os.getenv('DB_NAME', "librairy_api_db")
)
db = SQLAlchemy(app)


def create_table():
    with app.app_context():
        db.create_all()