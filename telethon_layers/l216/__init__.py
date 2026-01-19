"""
Слой 216: обёртка над исходниками Telethon 1.42.0 (копия).
Статические импорты нужны для подсказок типов.
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
    sessions,
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
    "sessions",
    "version",
    "sync",
]
