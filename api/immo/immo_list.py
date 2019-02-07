from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators

list = Blueprint('immo_list', __name__)

@list.route("/immo/list", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "list").json()
    if request.method == "GET":
        return ResponseObject(400, "list").json()
