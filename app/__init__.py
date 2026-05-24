from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prestamos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
        from app import models

    from app.route import main, auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    login_manager.login_view = 'auth.login'

    login_manager.init_app(app)

    return app