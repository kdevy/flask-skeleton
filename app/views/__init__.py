from flask import Blueprint
from app.views.login_view import LoginView
from app.views.register_view import RegisterView

user_bp = Blueprint("user", __name__, template_folder="../templates/user")

login_view = LoginView.as_view("user_view")
user_bp.add_url_rule("/login" \
                    , view_func=LoginView.as_view("login") \
                    , methods=["GET", "POST"])

register_view = RegisterView.as_view("register_view")
user_bp.add_url_rule("/register" \
                    , view_func=RegisterView.as_view("register") \
                    , methods=["GET", "POST"])