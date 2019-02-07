from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators

add = Blueprint('immo_add', __name__)

@add.route("/immo/add", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "add").json()
    if request.method == "GET":
        return ResponseObject(400, "add").json()
