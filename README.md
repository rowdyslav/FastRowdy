**FastRowdy**  
**Backend Template**  
*Modern API Development Blueprint with FastAPI + MongoDB*  

---

### 🛠 **Тех Стек**  
▸ **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
▸ **База данных**: [MongoDB](https://www.mongodb.com/)
▸ **ODM**: [Beanie](https://roman-right.github.io/beanie/)
▸ **Аутентификация**: [FastAPI Users](https://fastapi-users.github.io/fastapi-users/)  
▸ **Контейнеризация**: [Docker](https://www.docker.com/) + [Compose](https://docs.docker.com/compose/) 

---

### ⚡ **Быстрый Старт**  
1. Клонировать и настроить окружение:  
```bash
git clone https://github.com/your-account/fastrowdy.git
cd fastrowdy
cp .env.example .env
```
2. Запустить через Docker Compose:  
```bash
docker-compose -f docker/compose.yml up --build
```

---

### 🔧 **Конфигурация**  
`.env` файл должен содержать:  
```env
MONGODB_URL=mongodb://mongo:27017
SECRET_KEY=your-secure-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

### 🛡 **Аутентификация**  
Пример защищенного эндпоинта:  
```python
from fastapi import Depends
from fastapi_users import FastAPIUsers

@router.get("/protected")
async def protected_route(
    user: User = Depends(FastAPIUsers.current_user(active=True))
):
    return {"message": f"Hello {user.email}!"}
```
