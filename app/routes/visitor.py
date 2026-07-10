from flask import Blueprint

visitor_bp = Blueprint("visitor", __name__)

@visitor_bp.route("/")
def home():
    return "Bienvenido visitante"
