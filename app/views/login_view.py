from flask import request, jsonify, render_template
from flask.views import MethodView
from app.services.user_service import UserService

class LoginView(MethodView):
    def get(self):
        context = {}
        return render_template("login.html", **context)
    
    def post(self):
        data = request.form
        try:
            user = UserService.login(data.get("username"), data.get("password"))
            return jsonify({"message": "Logged in", "user": user})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
