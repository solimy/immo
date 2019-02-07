from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

get = Blueprint('user_get', __name__)

@get.route("/user/get", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "get").json()
    if request.method == "GET":
        return ResponseObject(400, "get").json()
