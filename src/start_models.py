# from models import *
from core.pic_handler import PicHandler
from core.student_handler import StudentHandler


if __name__ == '__main__':
    print(PicHandler.get_image_list(id_=2))
    # print(StudentHandler.get_user(user_id=1))
    # Base.metadata.create_all(bind=engine)
