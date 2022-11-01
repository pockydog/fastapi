from random import choice

from fastapi import WebSocket, APIRouter
from fastapi.responses import HTMLResponse
from core.websocket_handler import test, WebsocketHandler

ws_router = APIRouter(prefix='/websocket')
WebsocketHandler = WebsocketHandler()


@ws_router.get('/{user}')
async def get(user: str):
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
                var ws = new WebSocket("ws://localhost:8023/websocket/ws/""" + user + """");
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
    return HTMLResponse(html)


@ws_router.websocket('/ws/{user}')
async def websocket_endpoint(websocket: WebSocket, user: str):
    await test.connect(websocket)
    await test.broadcast(f'你好{user}')
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"你好_{data}")
        num = choice(test.member_info)
        print(num)
        await num.send_text(data)


@ws_router.websocket('ws/{user_id}')
async def websocket_talk(websocket: WebSocket, user_id: str):
    await test.connects(websocket, user_id)
    await websocket.send_text(f'開始與{user_id}對談')
    while True:
        await websocket.receive_text()
        await test.send_target(target=user_id)





