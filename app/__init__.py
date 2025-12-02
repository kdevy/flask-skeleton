import os
from dotenv import load_dotenv

env_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(env_file_path)

from flask import Flask
from myflaskbase.extensions import db
from myflaskbase import init_app
from app.config import ProjectConfig

def create_app(config=ProjectConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    init_app(app)

    with app.app_context():
        db.create_all()

    from app.views import index_bp
    app.register_blueprint(index_bp, url_prefix="/")

    return app