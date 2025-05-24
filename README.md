# Описание репозитория: Библиотечная система (React + Flask + PostgreSQL)

## Обзор проекта
Веб-приложение для управления библиотекой с современным стеком технологий. Система предоставляет REST API для учета книг, читателей и читальных залов, а также интуитивно понятный интерфейс для библиотекарей.

## Стек технологий
**Frontend**:  
- React 18 (TypeScript)  
- Redux Toolkit (управление состоянием)  
- Material-UI (компоненты интерфейса)  
- Axios (HTTP-клиент)  

**Backend**:  
- Python 3  
- Flask (REST API)  
- Flask-SQLAlchemy (ORM)  
- Flask-Marshmallow (сериализация)  

**База данных**:  
- PostgreSQL (основное хранилище)  
- Redis (кеширование)  

## Основные функциональные возможности

### API Endpoints (Flask)
- `GET /api/books` - список всех книг с фильтрацией  
- `POST /api/books` - добавление новой книги  
- `PUT /api/books/<id>` - обновление книги  
- `GET /api/readers` - управление читателями  
- `GET /api/halls` - информация о читальных залах  
- `POST /api/transactions` - операции выдачи/приема книг  

### Интерфейс (React)
- 📚 Управление каталогом книг (CRUD операции)  
- 👥 Регистрация читателей и выдача книг  
- 🏛 Просмотр загруженности читальных залов  
- 🔍 Поиск по книгам с расширенными фильтрами  
- 📊 Статистика и отчеты в реальном времени  

## Установка и запуск

### Требования
- Node.js 16+  
- Python 3.9+  
- PostgreSQL 13+  
- Redis 6+  

### Настройка backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
flask db upgrade  # Применение миграций
flask run
```

### Настройка frontend
```bash
cd frontend
npm install
npm start
```

## Структура проекта
```
library-system/
├── backend/              # Flask приложение
│   ├── app/              # Основной модуль
│   │   ├── models/       # Модели PostgreSQL
│   │   ├── routes/       # API endpoints  
│   │   └── services/     # Бизнес-логика
│   ├── migrations/       # Миграции базы данных
│   └── config.py         # Конфигурация
│
├── frontend/             # React приложение
│   ├── public/           # Статические файлы
│   ├── src/              # Исходный код
│   │   ├── features/     # Redux slices
│   │   ├── pages/        # Компоненты страниц
│   │   └── services/     # API клиент
│   └── tsconfig.json     # TypeScript конфиг
│
├── docker/               # Конфигурация Docker
└── docker-compose.yml    # Оркестрация сервисов
```

## Деплой
Проект готов к деплою на:
- Heroku  
- Vercel (frontend) + Render (backend)  
- Docker-контейнерах (включен docker-compose)  

## Лицензия
MIT License
