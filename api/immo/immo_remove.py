from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

remove = Blueprint('immo_remove', __name__)

@remove.route("/immo/remove", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "remove").json()
    if request.method == "GET":
        return ResponseObject(400, "remove").json()
