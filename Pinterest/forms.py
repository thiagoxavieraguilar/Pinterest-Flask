from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField,SubmitField,PasswordField,FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from .models import User

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    button = SubmitField('Login')


class FormSign(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 20)])
    confirm_password = PasswordField('Confirm_password', validators=[DataRequired(), EqualTo('password')])
    button = SubmitField('Sign up')

    def validate_email(self,email):
        user =  User.query.filter_by(email=email).first()
        if user:
            return ValidationError(flash('Email já cadastrado'))

class FormImg(FlaskForm):
    img = FileField("Foto", validators=[DataRequired()])
    button = SubmitField("Enviar")