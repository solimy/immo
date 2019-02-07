from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

edit = Blueprint('user_edit', __name__)

@edit.route("/user/edit", methods = ["GET", "POST"])
@decorators.test
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "edit").json()
