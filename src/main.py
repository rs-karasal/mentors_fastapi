from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_users import FastAPIUsers

from src.auth.manager import get_user_manager
from src.auth.auth import auth_backend
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate
from src.chat.router import router as chat_router


# TODO: cors


main_app = FastAPI(
    title="Mentores platform",
)


# Auth routers - Fastapi-Users
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


main_app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


main_app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


# Chat routers
main_app.include_router(chat_router)
