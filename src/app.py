from fastapi import FastAPI
from controllers import router

app = FastAPI()
app.include_router(router)


def create_app():
    return app
