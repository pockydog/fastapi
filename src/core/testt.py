# from fastapi import WebSocket, Cookie, Query
# from typing import Optional
#
# from starlette import status  # error code
#
#
# class WebsocketTest:
#     """先查詢對方是否有正確的cookie or token ， 若錯誤則raise """
#     async def get_cookie_or_token(self,
#                                   websocket: WebSocket,
#                                   session: Optional[str] = Cookie(None),
#                                   token: Optional[str] = Query(None),
#                                   ):
#         if session is None and token is None:
#             await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
#
#         return session or token



from typing import Optional

from fastapi import Cookie, Depends, FastAPI,Request, Query, WebSocket, status

from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse(
        "webchat.html",
        {
            "request": request
        }
    )


async def get_cookie_or_token(
    websocket: WebSocket,
    session: Optional[str] = Cookie(None),
    token: Optional[str] = Query(None),
):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token

@app.websocket("/items/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    cookie_or_token: str = Depends(get_cookie_or_token),
):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"消息是: {data}")



