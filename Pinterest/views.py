from flask import Flask,render_template,url_for, Blueprint
from flask_login import login_required

views = Blueprint("views", __name__)

@views.route("/",  methods=['GET', 'POST'])
@login_required
def home():
    return 'ok'