**# RowdyFullstack**  
**Fullstack Application Template**  
*Modern Web Development Blueprint for Python & TypeScript*  

---

### 🛠 **Технологический Стек**  

#### **Backend** (Python)  
▸ **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (ASGI)  
▸ **База данных**: [MongoDB](https://www.mongodb.com/) (NoSQL)  
▸ **ODM**: [BeanieODM](https://roman-right.github.io/beanie/) (Async MongoDB)  
▸ **Аутентификация**: [FastAPI Users](https://fastapi-users.github.io/fastapi-users/) (JWT/OAuth2)  
#### **Frontend** (TypeScript)  
▸ **Framework**: [React](https://react.dev/) (v18+)  

#### **Контейнеризация** (Docker)  
[Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/)  

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