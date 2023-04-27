
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import views
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get('DB_NAME') 


app =  Flask(__name__)
app.config['SECRET_KEY'] = "pinterest"

db = SQLAlchemy()


app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:root@localhost/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(views, url_prefix="/")

db.init_app(app)

