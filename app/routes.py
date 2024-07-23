from index import index
from play import play


def init_app(app):
    app.add_url_rule(
        "/",
        view_func=index,
        methods=["GET", "POST"],
    )
