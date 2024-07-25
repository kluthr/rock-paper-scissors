from flask import Flask

from app.routes import init_app


def create_app():
    # create flask app and register all routes
    app = Flask(__name__, template_folder="templates")
    init_app(app)
    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)
