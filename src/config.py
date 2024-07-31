import os

from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    load_dotenv(".env.example")


class Config:
    # Database Postgres
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")

    # FastAPI
    SECRET = os.environ.get("AUTH_SECRET_KEY")
    MANAGER_SECRET = os.environ.get("MANAGER_SECRET_KEY")


