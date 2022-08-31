from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

CLIENT_URL = config("CLIENT_URL", cast=str)

DATABASE_URL = config("DATABASE_URL", cast=str, default=None)

if DATABASE_URL is None:
    POSTGRES_USER = config("POSTGRES_USER", cast=str)
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
    POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="localhost")
    POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
    POSTGRES_DB = config("POSTGRES_DB", cast=str)

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
