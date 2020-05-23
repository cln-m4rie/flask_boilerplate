from typing import Tuple

from flask import Blueprint, Response, jsonify

from flask_boilerplate.handlers import health_check_handler

hc_bp = Blueprint("hc", __name__, url_prefix="/api/hc")


@hc_bp.route("", methods=["GET"])
def health_check() -> Tuple[Response, int]:
    ctx: dict = health_check_handler.handle_get_request()
    return jsonify(ctx)
