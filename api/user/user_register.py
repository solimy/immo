from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

register = Blueprint('user_register', __name__)

@register.route("/user/register", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "register").json()
    if request.method == "GET":
        return ResponseObject(400, "register").json()
