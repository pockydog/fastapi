from sqlalchemy import func, Column, Integer, String, Boolean, DateTime
from db_setting import Base


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(90), nullable=True)
    gender = Column(Boolean(), comment='0:男, 1:女')
    grade = Column(Integer, server_default='4', comment='年級 1:高一 2:高二 3:高三 4:尚未選擇')
    phone_number = Column(String(30), nullable=False)
    create_datetime = Column(DateTime, server_default=func.now())
    update_datetime = Column(DateTime, server_default=func.now(), onupdate=func.now())

