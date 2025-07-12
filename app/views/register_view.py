from flask import request, jsonify, render_template
from flask.views import MethodView
from app.services.user_service import UserService

class RegisterView(MethodView):
    def get(self):
        context = {}
        return render_template("register.html", **context)

    def post(self):
        data = request.form
        try:
            new_user = UserService.register(data)
            return jsonify({"message": "Registered", "user": new_user}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
