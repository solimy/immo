from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators

disconnect = Blueprint('user_disconnect', __name__)

@disconnect.route("/user/disconnect", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(400, "disconnect").json()
    if request.method == "GET":
        return ResponseObject(400, "disconnect").json()
