import uvicorn

from blacksheep.server import Application
from blacksheep.server.responses import text


app = Application()


@app.route('/http-route-example')
async def home(request):    # type: ignore[no-untyped-def]
    return text('HTTP route response')


if __name__ == '__main__':
    uvicorn.run("blacksheep_app:app", workers=10, log_level="warning")
