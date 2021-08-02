# First try to setup a for loop that echos back a message
from http.server import HTTPServer, BaseHTTPRequestHandler
from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello():
    return "Hello World!"




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555)


