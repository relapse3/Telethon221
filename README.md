# Telethon 221 (custom fork)

Форк `Telethon 1.42.0`, упакованный под импортом `telethon_221`, чтобы не конфликтовать с обычным Telethon и работать рядом, даже в одном venv.

## Development
- Правьте код в `telethon_221/telethon/`. Лицензию не трогаем.
- Обновляйте версию в `pyproject.toml` и `telethon_221/telethon/version.py` при изменениях (например, `1.42.0+layer221.1`).
- Локальная установка для проверки: `pip install -e .`

## Publishing / install from Git
- Push the repo to your private remote (SSH example): `git remote add origin git@your.git.host:you/telethon.git`
- Установка в других проектах напрямую из Git:
  - Последний main: `pip install git+ssh://git@your.git.host/you/telethon.git#egg=telethon-221`
  - Конкретный тег/релиз: `pip install git+ssh://git@your.git.host/you/telethon.git@v1.42.0+layer221.0#egg=telethon-221`
- В коде импортируется как `import telethon_221` (обёртка прокидывает API как у обычного Telethon).

## Notes
- Имя PyPI-пакета `telethon-221`, чтобы не пересекаться с `telethon`. В одном venv можно держать оба.
- Опциональная зависимость `cryptg` сохранена; ставьте `pip install .[cryptg]` или `#egg=telethon-221[cryptg]` в Git URL.
- Апстрим: https://github.com/LonamiWebs/Telethon — пригодится для diff при обновлениях.
