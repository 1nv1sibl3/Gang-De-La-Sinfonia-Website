from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My App</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>"""

if __name__ == "__main__":
    app.run()
