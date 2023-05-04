from Pinterest import db,login_manager
from sqlalchemy.sql import func
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return User.query.get(int(id_usuario))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    imgs = db.relationship('Img', backref='user', passive_deletes=True, lazy=True)
    


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(150), default="default.png")
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    id_user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)