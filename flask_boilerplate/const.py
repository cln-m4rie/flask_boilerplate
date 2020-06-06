from pathlib import Path
from typing import Optional


class Const:
    class PathConfig:
        _root_path = Path(__file__).resolve().parent
        _storage_path = Path(__file__).resolve().parent / "storage"

        @staticmethod
        def root_path() -> Path:
            return Const.PathConfig._root_path

        @staticmethod
        def log_path(fp: Optional[str] = None) -> Path:
            return (
                Const.PathConfig._storage_path / "logs" / fp
                if fp is not None
                else Const.PathConfig._storage_path / "logs"
            )
