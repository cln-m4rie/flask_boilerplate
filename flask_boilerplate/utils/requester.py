from typing import Any

from flask import request


class FlaskRequester:
    @classmethod
    def all(cls) -> dict:
        res: dict = request.args.to_dict(flat=True)
        if cls.is_post():
            req_data = request.form.to_dict(
                flat=True) or request.get_json(force=True)
            if isinstance(req_data, dict):
                res.update(req_data)
            elif isinstance(req_data, list):
                res.update({"data": req_data})
        return res

    @classmethod
    def get_request_data(cls, key: str, default: Any = None, required: bool = False) -> Any:
        res = None
        if cls.is_get():
            res = request.args.get(key, default)
        elif cls.is_post():
            r = request.form.to_dict(flat=True) or request.get_json(force=True)
            if r:
                res = r.get(key, default)
        if res is None and required:
            raise KeyError(f"{key} required")
        return res

    @staticmethod
    def is_get() -> bool:
        return request.method == "GET"

    @staticmethod
    def is_post() -> bool:
        return request.method == "POST"

    @staticmethod
    def is_put() -> bool:
        return request.method == "PUT"

    @staticmethod
    def is_patch() -> bool:
        return request.method == "PATCH"

    @staticmethod
    def is_delete() -> bool:
        return request.method == "DELETE"
