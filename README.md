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
### Backend (бот + API)
1. Встановіть залежності:
```
pip install -r requirements.txt
```
2. Запустіть API:
```
uvicorn api:app --reload
```
3. Запустіть бота:
```
python bot.py
```

### Frontend (повний Web App)
1. Встановіть Node.js та залежності:
```
npm install
```
2. Запустіть Web App:
```
npm run dev -- --host 0.0.0.0 --port 5173
```

Після запуску Web App буде доступний на `http://<server>:5173`. Для Telegram Web App потрібен HTTPS-домен, тому налаштуйте SSL та проксі (наприклад через Nginx).
