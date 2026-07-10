from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.models import Contact
from app import db

index_bp = Blueprint("index", __name__)


# Página pública de presentación
@index_bp.route("/")
def home():
    return render_template("index.html", user=current_user)

@index_bp.route('/submit', methods=['POST'])
def submit():
    name    = request.form['name']
    email   = request.form['email']
    message = request.form['message']
    
    new_message = Contact(name, email, message)
    db.session.add(new_message)
    db.session.commit()
    
    flash("Tu mensaje fue enviado exitosamente.", "success")
    return redirect(url_for("index.home"))

# Dashboard privado según rol
@index_bp.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "admin":
        return redirect(url_for("admin.dashboard"))
    elif current_user.role == "supervisor":
        return redirect(url_for("supervisor.dashboard"))
    elif current_user.role == "client":
        return redirect(url_for("client.dashboard"))
    else:
        return redirect(url_for("visitor.home"))
