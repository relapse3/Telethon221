"""
Телетон форк с импортом по имени `telethon_221`, чтобы жить рядом с обычным Telethon.
Все исходники лежат в подмодуле `telethon_221.telethon` (скопировано из Telethon 1.42.0).
Статические импорты здесь нужны, чтобы IDE/типизация видели реальные типы.
"""
from .telethon import (
    TelegramClient,
    Button,
    events,
    utils,
    errors,
    types,
    functions,
    custom,
    connection,
    version,
    sync,
)

__version__ = version.__version__
__all__ = [
    "TelegramClient",
    "Button",
    "types",
    "functions",
    "custom",
    "errors",
    "events",
    "utils",
    "connection",
    "version",
    "sync",
]
