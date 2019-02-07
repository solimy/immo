from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

disconnect = Blueprint('disconnect', __name__)

@disconnect.route("/disconnect", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "disconnect").json()
