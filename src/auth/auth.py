import os
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
SECRET = os.getenv("AUTH_SECRET_KEY")

cookie_transport = CookieTransport(cookie_name="mentores", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
