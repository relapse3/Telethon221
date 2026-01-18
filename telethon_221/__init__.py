"""
Телетон форк с импортом по имени `telethon_221`, чтобы жить рядом с обычным Telethon.
Все исходники лежат в подмодуле `telethon_221.telethon` (скопировано из Telethon 1.42.0).
"""
import importlib as _importlib
import sys as _sys

# Подтягиваем исходный модуль и пробрасываем публичное API.
_t = _importlib.import_module(".telethon", __name__)

# Регистрируем основные подмодули под префиксом telethon_221.*
for _name in (
    "client",
    "tl",
    "events",
    "errors",
    "functions",
    "types",
    "utils",
    "custom",
    "network",
    "sync",
    "crypto",
    "sessions",
    "extensions",
):
    _sys.modules[f"{__name__}.{_name}"] = _importlib.import_module(f".telethon.{_name}", __name__)

# Экспортируем ключевые объекты на корень telethon_221.
TelegramClient = _t.TelegramClient
Button = _t.Button
events = _t.events
utils = _t.utils
errors = _t.errors
types = _t.types
functions = _t.functions
custom = _t.custom
connection = _t.connection
version = _t.version
sync = _sys.modules[f"{__name__}.sync"]

__version__ = _t.__version__
__all__ = _t.__all__ + ["sync"]
