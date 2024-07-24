from index import index


def init_app(app):
    app.add_url_rule(
        "/",
        view_func=index,
        methods=["GET", "POST"],
    )
