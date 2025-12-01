from flask import request, jsonify, render_template
from flask.views import MethodView
from app.services.user_service import UserService

class IndexView(MethodView):
    def get(self):
        context = {}
        return render_template("index.html", **context)
