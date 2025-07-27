from fastapi import FastAPI
from api.routes import router
from db.init_db import init_db

init_db()
app = FastAPI()
app.include_router(router)

