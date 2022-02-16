from quart import Quart, request, Response 
from quart.templating import render_template_string

app = Quart(__name__)

@app.route('/')
async def index():
    return Response(open(__file__).read(),  mimetype="text/plain")

@app.route('/quiquart')
async def quiquart():
    quiquart = request.args.get("quiquart", "Hello, world")
    return await render_template_string(quiquart)