from fastapi import APIRouter, Depends

from core.student_handler import StudentHandler
from schema.student_schema import *

router = APIRouter(prefix='/student')


@router.get('/info')
def create_item():
    result = {'result': 'vicky'}
    return result


@router.get('/info/{user_id}')
def get_info(common: StudentInfoSchema = Depends(StudentInfoSchema)):
    result = StudentHandler.get_user(user_id=common.user_id)
    return result


@router.post('/add-user')
def add_info(common: StudentBasicSchema = Depends(StudentBasicSchema)):
    result = StudentHandler.add_user(
        name=common.name,
        gender=common.gender,
        grade=common.grade,
        phone_number=common.phone_number,
    )
    return result


@router.delete('delete/{name}')
def delete_info(common: StudentSchema = Depends(StudentSchema)):
    result = StudentHandler.del_user(name=common.name)
    return result


@router.put('update/{id}')
def update_info(common: StudentSchema = Depends(StudentSchema)):
    result = StudentHandler.update_info(name=common.name)
    return result

