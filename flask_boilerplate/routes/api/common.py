import traceback
from http import HTTPStatus

from flask import current_app, jsonify, logging, request


def before_request():
    """
    リクエストの前処理
    """
    logger = logging.create_logger(current_app)
    logger.info(f"start {current_app.name} :: {request.json}")


def after_request(response):
    """
    リクエストの後処理
    """
    logger = logging.create_logger(current_app)
    logger.info(
        f"end {current_app.name} :: httpStatusCode={response._status_code}, response={response.response}")
    return response


def exception_handler(ex):
    """
    共通例外処理
    """
    logger = logging.create_logger(current_app)

    # 予期せぬ例外発生時
    logger.error(traceback.format_exc())
    response = {"message": "undefined error occured."}

    return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR


def not_found_handler(ex):
    """
    存在しないURLへのアクセス
    """
    logger = logging.create_logger(current_app)

    logger.warning(f"not found {request.url}")
    response = {"message": "resource not found."}

    return jsonify(response), HTTPStatus.NOT_FOUND
