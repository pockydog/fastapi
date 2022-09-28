from fastapi import APIRouter, Depends

from core.student_handler import StudentHandler
from schema.student_schema import StudentInfoSchema

student_router = APIRouter(prefix='/student')


@student_router.get('/info')
def create_item():
    result = {'result': 'vicky'}
    return result


@student_router.get('/info/{user_id}')
def create_item(user_id: StudentInfoSchema = Depends(StudentInfoSchema)):
    result = StudentHandler.get_user(user_id=user_id)
    return result



