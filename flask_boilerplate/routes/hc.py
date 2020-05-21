from typing import Tuple

from flask import Blueprint, Response, jsonify

hc_bp = Blueprint("hc", __name__, url_prefix="/hc")


@hc_bp.route("", methods=["GET"])
def health_check() -> Tuple[Response, int]:
    return jsonify({"message": "ok"})
