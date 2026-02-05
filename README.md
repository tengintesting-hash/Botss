# Telegram Web App Casino Ecosystem

## Де вставити дані бота
Створіть файл `.env` (завантажується автоматично) або задайте змінні середовища:

```
BOT_TOKEN=ваш_токен_від_BotFather
ADMIN_TOKEN=секретний_токен_для_адмін_API
WEB_APP_URL=https://ваш-домен/telegram-webapp
```

- `BOT_TOKEN` — обовʼязковий. Без нього бот не запуститься.
- `ADMIN_TOKEN` — потрібен для доступу до адмін-API.
- `WEB_APP_URL` — посилання на Web App. Якщо не вказати, використовується `https://t.me/<username>/app`.

## Адмін-панель
Адмін-панель реалізована як API у FastAPI. Усі запити потребують заголовок:

```
X-Admin-Token: ваш_ADMIN_TOKEN
```

Доступні ендпоінти:
- `GET /admin/users` — користувачі
- `GET /admin/offers` — оффери
- `POST /admin/offers` — створити оффер
- `GET /admin/channels` — спонсорські канали
- `GET /admin/transactions` — транзакції

## Запуск
1. Встановіть залежності:
```
pip install -r requirements.txt
```
1. Запустіть API:
```
uvicorn api:app --reload
```
2. Запустіть бота:
```
python bot.py
```

## Web App
Компоненти Web App лежать у файлах:
- `Home.jsx`
- `Earn.jsx`
- `Wallet.jsx`
- `Admin.jsx`

Ви можете імпортувати їх у ваш React-проєкт.
