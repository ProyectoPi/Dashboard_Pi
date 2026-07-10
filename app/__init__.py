from flask import Flask
from .config import Config
from .models import db
from flask_login import LoginManager
from .sockets import init_sockets
from .models import User
from flask_migrate import Migrate
from .models import db

from .routes import auth, admin, supervisor, client, visitor, index

login_manager = LoginManager()
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    # Flask-Login necesita esta función para recuperar el usuario por ID
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar base de datos
    db.init_app(app)
    migrate = Migrate(app, db)

    # Inicializar login
    login_manager.init_app(app)

    # Registrar blueprints
    
    app.register_blueprint(index.index_bp) 
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(admin.admin_bp, url_prefix="/admin")
    app.register_blueprint(supervisor.supervisor_bp, url_prefix="/supervisor")
    app.register_blueprint(client.client_bp, url_prefix="/client")
    app.register_blueprint(visitor.visitor_bp, url_prefix="/visitor")

    # Inicializar sockets
    init_sockets(app)

    return app
