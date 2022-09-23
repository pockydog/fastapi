from fastapi import APIRouter
from fastapi import UploadFile

from core.pic_handler import PicHandler

router = APIRouter(prefix='/pic')


@router.post('/file')
def create_file(file: UploadFile):
    image = file.file
    description = file.content_type
    PicHandler.add_file(image=image, description=description)
    return {'filename': file.filename}
