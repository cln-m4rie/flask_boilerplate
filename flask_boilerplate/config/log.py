from typing import Dict

from ..const import Const

log_setting: Dict = {
    "version": 1,
    "formatters": {"file": {"format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"}},
    "handlers": {
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "file",
            "filename": str(Const.PathConfig.log_path("app.log")),
            "backupCount": 3,
            "when": "D",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["file"]},
}
