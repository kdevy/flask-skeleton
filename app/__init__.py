import os
from dotenv import load_dotenv

env_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(env_file_path)

from flask import Flask
from myflaskbase.extensions import db, login_manager
from myflaskbase import init_app
from app.user.models import User
from app.config import ProjectConfig

def create_app(config=ProjectConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    init_app(app)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = "user.login"

    from app.views import index_bp
    app.register_blueprint(index_bp, url_prefix="/")
    from app.user import user_bp
    app.register_blueprint(user_bp, url_prefix="/user")

    return app