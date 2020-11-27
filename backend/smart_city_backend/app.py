import os
from logging.config import dictConfig

from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from smart_city_backend.api import api


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "%(levelname)9s -- %(asctime)s - %(module)s - %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["wsgi"]},
        "smart_city_backend": {"level": "DEBUG", "handlers": ["wsgi"]},
    }
)


os.environ["wsgi.url_scheme"] = "http"


def create_app(config=None):
    app = Flask(__name__)
    # app.config["SERVER_NAME"] = "a.ru"
    app.config["PREFERRED_URL_SCHEME"] = "https"

    CORS(app)

    # load environment configuration
    if "WEBSITE_CONF" in os.environ:
        app.config.from_envvar("WEBSITE_CONF")

    # load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith(".py"):
            app.config.from_pyfile(config)

    setup_app(app)

    return app


def setup_app(app):
    api.init_app(app)



app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8008, debug=True)
