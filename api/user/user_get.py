from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

get = Blueprint('user_get', __name__)

@get.route("/user/get", methods = ["GET", "POST"])
@decorators.test
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "get").json()
