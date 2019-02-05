from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"status":200, "toto":[1, 2, 3, 4]})
