from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators

edit = Blueprint('user_edit', __name__)

@edit.route("/user/edit", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "edit").json()
    if request.method == "GET":
        return ResponseObject(400, "edit").json()
