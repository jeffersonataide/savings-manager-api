from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_db import init_db


from app.api import portfolios
from app.config import settings


init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.client_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(portfolios.router)


@app.get("/")
def hello():
    return {"message": "savings manager api"}
