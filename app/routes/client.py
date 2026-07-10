from flask import Blueprint
from app.utils.decorators import role_required

client_bp = Blueprint("client", __name__)

@client_bp.route("/dashboard")
@role_required("client")
def dashboard():
    return "Panel de cliente"
