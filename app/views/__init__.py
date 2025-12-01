from flask import Blueprint
from flask_login import login_required
from app.views.user.login_view import LoginView
from app.views.user.register_view import RegisterView
from app.views.user.logout_view import LogoutView
from app.views.user.home_view import HomeView
from app.views.index.index_view import IndexView

user_bp = Blueprint("user", __name__, template_folder="../templates/user")

login_view = LoginView.as_view("login")
user_bp.add_url_rule("/login" \
                    , view_func=login_view \
                    , methods=["GET", "POST"])

register_view = RegisterView.as_view("register")
user_bp.add_url_rule("/register" \
                    , view_func=register_view \
                    , methods=["GET", "POST"])

logout_view = LogoutView.as_view("logout")
logout_view = login_required(logout_view)
user_bp.add_url_rule("/logout" \
                    , view_func=logout_view \
                    , methods=["GET"])

home_view = HomeView.as_view("home")
home_view = login_required(home_view)
user_bp.add_url_rule("/home" \
                    , view_func=home_view \
                    , methods=["GET"])


index_bp = Blueprint("index", __name__, template_folder="../templates/index")
index_bp.add_url_rule("/" \
                    , view_func=IndexView.as_view("index") \
                    , methods=["GET"])
