from typing import Optional
from models.models import Student
from db_setting import session

db = session


class StudentHandler:
    @staticmethod
    def common_parameters(id_: int = 10):
        return {'id': id_}

    @staticmethod
    def get_user(user_id):
        conditions = list()
        result_list = list()
        if user_id:
            conditions.append(Student.id == user_id)
        obs = db.query(Student).filter(*conditions).first()
        result = {
            'id': obs.id,
            'name': obs.name,
            }
        result_list.append(result)

        return result_list



