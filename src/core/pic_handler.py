from models.models import ProductPic
from db_setting import session
from PIL import Image, ImageFilter
from fastapi.responses import StreamingResponse
from io import BytesIO


from config import Config


class PicHandler:
    PATH = Config.IMAGE_PATH

    @classmethod
    def add_file(cls, image, description=None, remark='test'):
        pic = ProductPic(
            description=description,
            remark=remark
        )
        session.add(pic)
        session.flush()
        with open(f'{cls.PATH}/{pic.id}.jpg', 'wb') as file:
            pics = image.read()
            file.write(pics)
        session.commit()
        return {'success': 'True'}

    @classmethod
    def get_image_list(cls, id_=None):
        condition = list()
        result_list = list()
        if id_:
            condition.append(ProductPic.id == id_)
        info_list = session.query(ProductPic).filter(*condition).all()
        for info in info_list:
            result = {
                'id': info.id,
                'description': info.description,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def send_image(cls, id_):
        original_image = Image.open(f'{cls.PATH}/{id_}.jpg')
        original_image = original_image.filter(ImageFilter.BLUR)

        filtered_image = BytesIO()
        original_image.save(filtered_image, "JPEG")
        filtered_image.seek(0)

        return StreamingResponse(filtered_image, media_type="image/jpeg")




