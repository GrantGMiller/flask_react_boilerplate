# To start the backend server locally run
# cd backend
# pipenv shell
# python main.py
import time
from flask import Flask, jsonify

app = Flask("Flask React Boilerplate")


@app.route("/")
def index():
    return "Hello, World! the time is" + time.asctime()


@app.route("/get_time")
def get_time():
    return jsonify({"time": time.asctime()})


if __name__ == "__main__":
    app.run(port=9000, debug=True)
