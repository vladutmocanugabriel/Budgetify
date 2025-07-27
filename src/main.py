from fastapi import FastAPI
from api.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.include_router(router)

