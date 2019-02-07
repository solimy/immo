from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

edit = Blueprint('immo_edit', __name__)

@edit.route("/immo/edit", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "edit").json()
    if request.method == "GET":
        return ResponseObject(400, "edit").json()
