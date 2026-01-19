"""
Слой 220: пока копия исходников Telethon 1.42.0, готовая к замене на схему слоя 220.
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
