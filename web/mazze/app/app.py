from flask import render_template_string, Flask
app = Flask(__name__)


@app.route("/<path>")
def index(path):
    if "flag" in path:
        contnt = "<h1>Hello H4ck3r !</h1><p>I guess you want this: 515778776147464456455a37597a42744d313877626c397064484e66626d39305833526f4e4852665a54527a6558304b3d3d</p>"
    elif path:
        contnt = "<h1>Page Note Found</h1><p>this page ( {} ) does not exist !<p> ".format(
            path)
    template = f''' 
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <title>Fake Maze</title>
                    </head>
                    <body>
                        {contnt}
                    </body>
                    </html>
                '''
    return render_template_string(template)
