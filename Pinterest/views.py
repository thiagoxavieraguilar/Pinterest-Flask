from flask import Flask,render_template,url_for, Blueprint,redirect,flash
from flask_login import login_required, login_user, logout_user, current_user
from Pinterest import bcrypt, db,app
from Pinterest.forms import  FormLogin,FormSign,FormImg
from Pinterest.models import  User, Img
from werkzeug.utils import secure_filename
import os

views = Blueprint("views", __name__)

@views.route("/", methods=['GET', 'POST'])
@views.route("/homepage", methods=['GET', 'POST'])
def homepage():
    """
    Displays the homepage and allows the user to log in.
    """
    form_login = FormLogin()
    if form_login.validate_on_submit():
        db_user = User.query.filter_by(email=form_login.email.data).first()
        if db_user and bcrypt.check_password_hash(db_user.password, form_login.password.data):
            login_user(db_user, remember=True)
            return redirect(url_for('views.perfil', user_id=db_user.id))
        else:
            flash('No user with this email')
            return redirect(url_for('views.creat_account'))

    return render_template('homepage.html', form=form_login)

@views.route("/creat_account", methods=['GET', 'POST'])
def creat_account():
    """
    Displays the signup form and creates a new user when the form is submitted.
    """
    form_sign = FormSign()
    if form_sign.validate_on_submit():
        try:
            hashed_password  = bcrypt.generate_password_hash(form_sign.password.data).decode('utf-8')
            user = User(email=form_sign.email.data, username=form_sign.username.data, password=hashed_password )
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created successfully!', 'success')
            return redirect(url_for('views.perfil', user_id=user.id))
        except:
            db.session.rollback()
            flash('Error creating account. Please try again later.')
            return redirect(url_for('views.homepage'))
    return render_template('creat_account.html', form=form_sign)

@views.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    """
    Logs out the user and redirects to the homepage.
    """
    logout_user()
    return redirect(url_for('views.homepage'))

@views.route("/perfil/<int:user_id>", methods=['GET', 'POST'])
def perfil(user_id):
    if user_id == current_user.id:
        # User looking at own profile
        form_img = FormImg()
        if form_img.validate_on_submit():
            try:
                file = form_img.img.data
                secure_name = secure_filename(file.filename)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], secure_name)
                file.save(path)
                img = Img(image=secure_name, id_user=current_user.id)
                db.session.add(img)
                db.session.commit()
                flash('Image uploaded successfully!', 'success')
            except Exception as e:
                flash(f'Error uploading image: {str(e)}', 'danger')
        return render_template('perfil.html', user=current_user, form=form_img)
    else:
        user = User.query.get(user_id)
        return render_template('perfil.html', user=user)

@views.route("/feed", methods=['GET', 'POST'])
@login_required
def feed():
    """
    Displays the all images in a  feed for the logged-in user.
    """
    imgs =  Img.query.order_by(Img.date_created).all()
    return render_template('feed.html', fotos=imgs)