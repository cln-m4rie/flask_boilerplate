from logging.config import dictConfig

from flask import Flask
from flask_cors import CORS

from flask_boilerplate.config.log import log_setting
from flask_boilerplate.envs import DEBUG, SECRET_KEY

from .routes.hc import hc_bp

app = Flask(__name__)

app.register_blueprint(hc_bp)

app.config["JSON_AS_ASCII"] = False
app.config["DEBUG"] = DEBUG
app.static_url_path = "/static/"
app.secret_key = SECRET_KEY

dictConfig(log_setting)


@app.route("/robots.txt")
def display_robots_txt():
    return app.send_static_file("robots.txt")


@app.route("/favicon.ico")
def display_favicon():
    return app.send_static_file("favicon.ico")


CORS(app)
