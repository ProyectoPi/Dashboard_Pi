from flask import Blueprint, render_template
from app.utils.decorators import role_required
from flask_login import current_user, login_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/dashboard")
# @role_required("admin")
@login_required
def dashboard():
    return render_template("dashboard/home.html", user=current_user)

@admin_bp.route("/projects")
@login_required
def projects():
    return render_template("dashboard/projects.html", user=current_user)

@admin_bp.route("/structure")
@login_required
def structure():
    return render_template("dashboard/structure.html", user=current_user)

@admin_bp.route("/map")
@login_required
def map():
    return render_template("dashboard/map.html", user=current_user)

@admin_bp.route("/charts")
@login_required
def charts():
    return render_template("dashboard/charts.html", user=current_user)

@admin_bp.route("/matrixes")
@login_required
def matrixes():
    return render_template("dashboard/matrixes.html", user=current_user)

@admin_bp.route("/comparisons")
@login_required
def comparisons():
    return render_template("dashboard/comparisons.html", user=current_user)

@admin_bp.route("/forecasts")
@login_required
def forecasts():
    return render_template("dashboard/forecasts.html", user=current_user)
