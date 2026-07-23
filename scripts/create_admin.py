import os
from app import create_app
from app.models import db, User, Role
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    u, p = os.environ["ADMIN_USER"], os.environ["ADMIN_PASS"]
    if User.query.filter_by(username=u).first():
        print(f"'{u}' ya existe."); raise SystemExit
    db.session.add(User(username=u, password=generate_password_hash(p), role=Role.ADMIN))
    db.session.commit()
    print(f"Admin '{u}' creado.")
