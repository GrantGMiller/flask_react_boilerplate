# To start the backend server locally run
# cd backend
# pipenv shell
# python main.py
import time
from flask import Flask, jsonify, send_from_directory

app = Flask(
    "Flask React Boilerplate",
    static_folder="./frontend/build",
    static_url_path="/",
)


@app.route("/")
def serve_index():
    print("server index")
    print('app.static_folder:', app.static_folder)
    return send_from_directory(app.static_folder, "index.html")


@app.route("/get_time")
def get_time():
    return jsonify({"time": time.asctime()})


if __name__ == "__main__":
    app.run(port=9000, debug=True)
