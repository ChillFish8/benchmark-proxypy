import uvicorn

from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Route


async def homepage(request):
    return Response('Hello, world!', media_type='text/plain')


app = Starlette(debug=True, routes=[
    Route('/http-route-example', homepage),
])


if __name__ == '__main__':
    uvicorn.run("starlette_app:app", workers=10, log_level="warning")
