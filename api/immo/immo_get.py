from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

get = Blueprint('immo_get', __name__)

@get.route("/immo/get", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "get").json()
