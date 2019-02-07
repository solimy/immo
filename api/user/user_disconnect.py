from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

disconnect = Blueprint('user_disconnect', __name__)

@disconnect.route("/user/disconnect", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "disconnect").json()
    if request.method == "GET":
        return ResponseObject(400, "disconnect").json()
