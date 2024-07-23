from flask import Flask

import routes


def create_app():
    """
    Create the flask app and register all routes

    Configurations would go here in a more complex app
    """
    app = Flask(__name__, template_folder="templates")
    routes.init_app(app)
    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)
