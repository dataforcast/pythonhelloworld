from flask import Flask
from core import hello
import os

# Port is retrieved from environment
PORT = int(os.environ.get('PORT', 80))
app = Flask(__name__)

@app.route('/')
def hello_world():
    return hello.hello_world()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
