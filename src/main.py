from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.database import User
from auth.schemas import UserRead, UserCreate


main_app = FastAPI(
    title="Mentores platform",
)


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
