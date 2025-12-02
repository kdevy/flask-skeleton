from flask import Blueprint
from app.views.index.index_view import IndexView
from app.views.index.hoge_view import HogeView

index_bp = Blueprint("index", __name__, template_folder="../templates/index")
index_bp.add_url_rule("/" \
                    , view_func=IndexView.as_view("index") \
                    , methods=["GET"])
index_bp.add_url_rule("/hoge" \
                    , view_func=HogeView.as_view("hoge") \
                    , methods=["GET"])
