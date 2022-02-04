from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/fastapi/app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    await request.send_push_promise("/static/home.css")
    await request.send_push_promise(
        "./static/flag_1029390EBB523BBC668DEEFABE493722.css")
    return HTMLResponse("""<html>
                        <head>
                            <title>Promise</title>
                            <link rel="stylesheet" href="/static/home.css"/>
                        </head>
                        <body>
                            <div>
                                <div class="container">
                                    HTTP?
                                </div>
                            </div>
                        </body>
                        </html>
                        """)