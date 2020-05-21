from flask import Flask

from .routes.hc import hc_bp

app = Flask(__name__)

app.register_blueprint(hc_bp)

app.config["JSON_AS_ASCII"] = False
