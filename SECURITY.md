# Безопасность

## Как сообщить об уязвимости

Не открывайте публичный issue. Нажмите «Report a vulnerability» на вкладке **Security** или напишите мне в Telegram: [@BehruzAvezmatov](https://t.me/BehruzAvezmatov).

## Что сделано

- Создавать, редактировать и удалять статьи могут только сотрудники (`is_staff`), остальные попадают на вход.
- `SECRET_KEY` берётся из `.env`, без него сайт не стартует; `DEBUG` по умолчанию выключен, `ALLOWED_HOSTS` задаётся явно.
- Формы защищены CSRF-токеном Django, ссылка на картинку проверяется `URLField`.

GitHub Actions на каждый push запускает тесты, `pip-audit` и `gitleaks` по всей истории.
