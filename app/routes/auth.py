from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_user, logout_user
from app.models import User

from werkzeug.security import check_password_hash
from flask_login import login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("index.dashboard"))
        else:
            return "Credenciales inválidas", 401
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    # return redirect(url_for("auth.login"))
    return redirect(url_for("index.home"))