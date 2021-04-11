from flask import Flask
from createUser import init
app = Flask(__name__)

@app.route('/')
def hello_world():
    path = init()
    return 'Hello, World!: '+str(path)
