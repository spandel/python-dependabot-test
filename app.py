from flask import Flask
from gevent import pywsgi

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    LOCALHOST = '0.0.0.0'
    PORT = 8080
    
    APP_SERVER = pywsgi.WSGIServer((LOCALHOST, PORT), app)
    APP_SERVER.serve_forever()