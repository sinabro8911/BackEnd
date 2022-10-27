from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'hello'

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)