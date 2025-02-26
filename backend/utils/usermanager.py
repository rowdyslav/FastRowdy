from typing import Optional

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users_db_beanie import BeanieUserDatabase, ObjectIDIDMixin
from icecream import ic

from backend.config import settings
from backend.schemas.models import User

SECRET = settings.SECRET_KEY


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        ic(f"User {user.id} has registered.")


async def get_user_db():
    yield BeanieUserDatabase(User)  # type: ignore


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])
current_optional_user = fastapi_users.current_user(optional=True)
current_active_user = fastapi_users.current_user(active=True)
