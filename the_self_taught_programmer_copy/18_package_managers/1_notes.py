from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


app.run(port='8000')

# import sys
# print(sys.executable)