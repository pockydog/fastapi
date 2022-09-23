from models.models import ProductPic
from db_setting import session
from config import Config


class PicHandler:
    @classmethod
    def add_file(cls, image, description=None):
        pic = ProductPic(
            description=description
        )
        session.add(pic)
        session.flush()
        image.save(f'{Config.IMAGE_PATH}/{pic.id}.jpg')
        session.commit()
        return {'success': 'True'}


