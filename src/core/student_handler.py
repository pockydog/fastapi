from models.models import Student
from db_setting import session
from const import Const

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

    @classmethod
    def add_user(cls, name, gender, grade, phone_number):
        cls.validate_user(method=Student, grade=grade, phone=phone_number)
        obj = Student(
            name=name,
            gender=gender,
            grade=grade,
            phone_number=phone_number,
        )
        session.add(obj)
        session.flush()
        result = {
            'id': obj.id,
            'name': obj.name,
            'gender': obj.gender,
            'grade': obj.grade,
            'phone_number': obj.phone_number,
        }
        session.commit()

        return result

    @classmethod
    def validate_user(cls, method, phone, grade):
        validate_phone = db.query(method).filter(Student.phone_number == phone).first()
        if validate_phone:
            raise Exception('User already exist')
        if grade not in Const.Grade.get_elements():
            raise Exception('Only 1-3 grade')






