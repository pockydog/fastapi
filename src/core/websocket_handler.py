from typing import List, Dict

from fastapi import WebSocket

from models.models import Student
from db_setting import session

from models.models import Student

db = session


class WebsocketHandler:
    @classmethod
    def get_user(cls, user_id):
        user = db.query(Student).filter(Student.id == user_id).first()
        return user


class WebsocketHandler:
    def __init__(self):
        # 儲存激活的ws連線對象
        self.member_infos: List[Dict[str, WebSocket]] = list()
        self.member_info = list()

    async def connect(self, ws: WebSocket):
        # 等待連線
        await ws.accept()
        # 儲存連線對象
        self.member_info.append(ws)

    async def connects(self, ws: WebSocket):
        # 等待連線
        await ws.accept()
        # 儲存連線對象（加入id）
        id_ = ws.headers.get('id')
        user = session.query.filter(Student.id == id_).first()
        self.member_infos[user.id] = ws

    async def broadcast(self, message: str):
        """廣播"""
        for member in self.member_info:
            await member.send_text(message)

    async def send_target(self, message: str, ws: WebSocket, target: str):
        target_id = db.query(Student).filter(Student.id == target).first()
        await ws.accept()
        for user in self.member_info:
            if user['user'] == target_id:
                await user['ws'].send_text(message)

    async def send_someone(self, message: str, ws: WebSocket, target: int):
        target_id = db.query(Student).filter(Student.id == target).first()
        Test.connects
        await ws.accept()
        while True:
            await target_id['ws'].send_text(message)


test = Test()
