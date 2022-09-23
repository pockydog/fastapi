from fastapi import APIRouter

from core.student_handler import StudentHandler
from db_setting import session

router = APIRouter(prefix='/student')


@router.get('/info')
def create_item():
    result = {'result': 'vicky'}
    return result


@router.get('/info/{user_id}')
def create_item(user_id: int):
    result = StudentHandler.get_user(user_id=user_id)
    return result
