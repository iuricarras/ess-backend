import asyncio

from websockets.asyncio.server import serve


async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)


async def startWS():
    async with serve(handler, "", 8001) as server:
        await server.serve_forever()

