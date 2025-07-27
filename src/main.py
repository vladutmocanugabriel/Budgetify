from fastapi import FastAPI
from api.routes import router



app = FastAPI(title="Budgetify API")

app.include_router(router)