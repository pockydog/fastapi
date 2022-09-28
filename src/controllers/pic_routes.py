from typing import Optional, Union

from fastapi import APIRouter, Depends
from fastapi import UploadFile, File

from core.pic_handler import PicHandler
from schema.student_schema import PicTestSchema


pic_router = APIRouter(prefix='/pic')


@pic_router.post('/file')
def create_file(file: UploadFile):
    image = file.file
    description = file.content_type
    PicHandler.add_file(image=image, description=description)
    return {'filename': file.filename}


@pic_router.post("/uploadfile")
def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@pic_router.post("/files")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@pic_router.get('/get-info/{id_}')
def get_info(id_=int):
    result = PicHandler.get_image_list(id_=id_)
    return result


@pic_router.post('/send-image')
def send_image(id_: Union[int, None] = None):
    result = PicHandler.send_image(id_=id_)
    return result

