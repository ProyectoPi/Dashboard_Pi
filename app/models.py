from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Role:
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    CLIENT = "client"
    VISITOR = "visitor"

class User(UserMixin, db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role     = db.Column(db.String(20), nullable=False, default=Role.VISITOR)
    
    
class Contact(db.Model):
    id      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name    = db.Column(db.String(100), unique=False, nullable=False)
    email   = db.Column(db.String(200), unique=False, nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    def __init__(self, name, email, message):
        self.name    = name
        self.email   = email
        self.message = message 
