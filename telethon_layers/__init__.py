"""
telethon_layers: сборка нескольких слоёв Telethon под разными именами, чтобы их можно было импортировать рядом.
Примеры:
    from telethon_layers.l221 import TelegramClient, types
    from telethon_layers.l220 import TelegramClient as Client220
"""

from . import l221, l220

__all__ = ["l221", "l220"]
