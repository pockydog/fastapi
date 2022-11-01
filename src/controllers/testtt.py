from fastapi import APIRouter, Depends


ws_router = APIRouter(prefix='/websocket')

@ws_router.websocket('/test')

