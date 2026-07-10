from flask import Blueprint
from app.utils.decorators import role_required

supervisor_bp = Blueprint("supervisor", __name__)

@supervisor_bp.route("/dashboard")
@role_required("supervisor")
def dashboard():
    return "Panel de supervisor"
