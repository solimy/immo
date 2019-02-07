from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators

get = Blueprint('immo_get', __name__)

@get.route("/immo/get", methods = ["GET", "POST"])
@decorators.debug_request_display
def handle():
    if request.method == "POST":
        return ResponseObject(400, "get").json()
    if request.method == "GET":
        return ResponseObject(400, "get").json()
