from fastapi import FastAPI

# from pydantic import BaseModel

from core.student_hanlder import StudentHandler

app = FastAPI()


@app.get('/info')
def create_item():
    result = {'result': 'vicky'}
    return result


# @app.get('/info/{user_id}')
# def create_item(user_id: int):
#     result = StudentHandler.get_user(db=session, user_id=user_id)
#     return result
