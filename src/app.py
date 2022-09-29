from fastapi import FastAPI
from controllers import *

app = FastAPI()
# app.include_router(student_router)
# app.include_router(pic_router)
app.include_router(ws_router)


def create_app():
    return app
