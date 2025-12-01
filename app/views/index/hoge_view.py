from flask import render_template
from flask.views import MethodView

class HogeView(MethodView):
    def get(self):
        context = {}
        return render_template("hoge.html", **context)
