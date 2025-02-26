**# RowdyFullstack**  
**Fullstack Application Template**  
*Modern Web Development Blueprint for Python & TypeScript*  

---

### 🛠 **Технологический Стек**  

#### **Backend** (Python)  
▸ **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (ASGI)  
▸ **База данных**: [MongoDB](https://www.mongodb.com/) (NoSQL)  
▸ **ORM/ODM**: [BeanieODM](https://roman-right.github.io/beanie/) (Async MongoDB)  
▸ **Аутентификация**: [FastAPI Users](https://fastapi-users.github.io/fastapi-users/) (JWT/OAuth2)  
▸ **Контейнеризация**: [Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/)  

#### **Frontend** (TypeScript)  
▸ **Framework**: [React](https://react.dev/) (v18+)  
▸ **Стили**: CSS-in-JS / [Tailwind](https://tailwindcss.com/) (опционально)  
▸ **Состояние**: [Redux Toolkit](https://redux-toolkit.js.org/) или [Zustand](https://zustand-demo.pmnd.rs/)  
▸ **Роутинг**: [React Router](https://reactrouter.com/)  

---

### 🚀 **Особенности**  
- **Полноценная аутентификация**:  
  ∙ Регистрация/Вход  
  ∙ Верификация email  
  ∙ Сброс пароля  
  ∙ JWT-токены  
- **Асинхронный API**: Async/Await для MongoDB  
- **Готовый Docker-образ**:  
  ∙ Оптимизированные слои  
  ∙ Раздельные сервисы для BE/FE  
  ∙ Автоматический деплой  
- **Type Safety**:  
  ∙ Pydantic v2 (Python)  
  ∙ Полная типизация TS (Frontend)  

---

### 📂 **Структура Проекта**  
```bash
rowdy-fullstack/
├── backend/               # FastAPI сервис
│   ├── app/              # Основная логика
│   │   ├── models/       # Beanie-документы
│   │   ├── routes/       # API эндпоинты
│   │   └── core/         # Конфиги, утилиты
│   └── requirements.txt  # Зависимости
│
├── frontend/             # React приложение
│   ├── src/              # Исходники
│   │   ├── api/          # API клиент
│   │   ├── store/        # State-менеджмент
│   │   └── views/        # Компоненты
│   └── package.json      # NPM зависимости
│
└── docker/               # Docker-окружение
    ├── compose.yml       # Мультисервисная конфигурация
    └── nginx/            # Reverse Proxy (опционально)
```

---

### ⚡ **Быстрый Старт**  
1. Клонировать репозиторий:  
   ```bash
   git clone https://github.com/your-account/rowdy-fullstack.git
   cd rowdy-fullstack
   ```

2. Запустить в Docker:  
   ```bash
   docker-compose -f docker/compose.yml up --build
   ```

3. Открыть в браузере:  
   ▸ API: `http://localhost:8000/docs`  
   ▸ Frontend: `http://localhost:3000`

---

### 💡 **Рекомендации по Разработке**  
- Для локальной разработки без Docker:  
  ```bash
  # Backend
  cd backend && uvicorn app.main:app --reload
  
  # Frontend
  cd frontend && npm start
  ```
  
- **Env-переменные**:  
  ```env
  # .env.backend
  MONGODB_URL=mongodb://localhost:27017
  SECRET_KEY=your-secure-key
  ```

---

### 📜 **Лицензия**  
MIT License · [![GitHub](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

*Адаптируйте шаблон под свои нужды. Удачной разработки!* 🚀