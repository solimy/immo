from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

edit = Blueprint('immo_edit', __name__)

@edit.route("/immo/edit", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "edit").json()
