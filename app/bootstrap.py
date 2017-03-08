"""Factory module creating flask app."""
import os
from flask import Flask


def bootstrap():
    """Factory function."""
    instance_path = os.path.abspath(
        os.path.join(__file__, os.pardir, "config"))
    app = Flask(__name__, instance_path=instance_path,
                instance_relative_config=True)

    _load_app_config(app)

    from app.api import api as api_blueprint
    from app.index import ind as index_blueprint

    app.register_blueprint(api_blueprint)
    app.register_blueprint(index_blueprint)
    return app


def _load_app_config(app):
    app.config.from_object("config.app.default")
    app.config.from_envvar("APP_CONFIG", silent=True)
    app.config["VERSION"] = os.environ.get("VERSION", "local")
    app.config["HOSTNAME"] = os.environ.get("HOSTNAME")
