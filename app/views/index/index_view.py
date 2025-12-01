from flask import render_template
from flask.views import MethodView
from flask import current_app, url_for

class IndexView(MethodView):

    def list_routes(self):
        routes = []
        for rule in current_app.url_map.iter_rules():
            if rule.endpoint == "static":
                continue

            methods = sorted(m for m in rule.methods if m not in ("HEAD", "OPTIONS"))

            dummy_kwargs = {arg: f"<{arg}>" for arg in rule.arguments}
            try:
                url = url_for(rule.endpoint, **dummy_kwargs)
            except Exception:
                url = str(rule)

            routes.append({
                "endpoint": rule.endpoint,
                "rule": str(rule),
                "url": url,
                "methods": methods,
            })
        return routes
    def get(self):
        context = {"routes": self.list_routes()}
        return render_template("index.html", **context)
