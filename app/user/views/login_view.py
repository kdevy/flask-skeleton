from flask import jsonify, render_template
from flask.views import MethodView
from app.user.services import UserService
from app.user.forms import LoginForm
from flask_babel import gettext

class LoginView(MethodView):
    form = None

    def dispatch_request(self, *args, **kwargs):
        self.form = LoginForm()
        return super().dispatch_request(*args, **kwargs)

    def get(self):
        context = {"form": self.form}
        return render_template("user/login.html", **context)

    def post(self):
        data = None
        try:
            if self.form.validate_on_submit():
                data = self.form.data
            else:
                raise ValueError(gettext("Invalid form submission"))

            user = UserService.login(data.get("username"), data.get("password"))
            return jsonify({"message": gettext("Logged in"), "user": user})
        except ValueError as e:
            return jsonify({"error": self.form.errors}), 200
