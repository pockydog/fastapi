from typing import Union, Optional


class PicTestSchema:
    def __init__(self, name: Optional[str] = None, bool: Union[bool, None] = None):
        self.name = name
        self.bool = bool


class StudentInfoSchema:
    def __init__(self, user_id: Union[int, None] = None):
        self.user_id = user_id
