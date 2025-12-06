from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from myflaskbase.extensions import db
from app.user.models import User
from flask_babel import gettext

class UserService:
    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            raise ValueError(gettext("Invalid credentials"))
        login_user(user)
        return {"username": username}

    @staticmethod
    def register(data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise ValueError(gettext("Username and password are required"))

        user = User.query.filter_by(username=username).first()

        if user:
            raise ValueError("User already exists")

        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return {"username": username}
