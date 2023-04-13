import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    if os.environ.get('FLASK_ENV') == 'development':
        app.run()
