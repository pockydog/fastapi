from typing import Union, Optional


class PicTestSchema:
    def __init__(self, name: Optional[str] = None, bool: Union[bool, None] = None):
        self.name = name
        self.bool = bool


class StudentInfoSchema:
    def __init__(self, user_id: Union[int, None] = None):
        self.user_id = user_id


class StudentBasicSchema:
    def __init__(self, name: str, gender: bool, grade: int, phone_number: Union[str, None] = 0):
        self.name = name
        self.gender = gender
        self.grade = grade
        self.phone_number = phone_number


class StudentSchema:
    def __init__(self, name: Union[str, None] = None):
        self.name = name



