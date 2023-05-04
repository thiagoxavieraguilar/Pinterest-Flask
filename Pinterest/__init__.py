
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


load_dotenv()

DB_NAME = os.environ.get('DB_NAME') 


app =  Flask(__name__)
app.config['SECRET_KEY'] = "pinterest"

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "homepage"

db = SQLAlchemy()


app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:root@localhost/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

db.init_app(app)

from .views import views
app.register_blueprint(views, url_prefix="/")

