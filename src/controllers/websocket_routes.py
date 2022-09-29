from fastapi import WebSocket, APIRouter
from fastapi.responses import HTMLResponse

ws_router = APIRouter(prefix='/websocket')


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8023/websocket/ws/user1");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class Test:
    def __init__(self):
        self.member_info: list[WebSocket] = list()

    def connect(self, ws: WebSocket):
        ws.accept()
        self.member_info.append(ws)

    def broadcast(self, message: str):
        for c in self.member_info:
            c.send_text(message)


test = Test()


@ws_router.get('/')
async def get():
    return HTMLResponse(html)


@ws_router.websocket('/ws/{user}')
def websocket_endpoint(websocket: WebSocket, user: str):
    test.connect(websocket)
    test.broadcast(f'{user}')


# @ws_router.websocket('/ws')
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"你好{data}")

