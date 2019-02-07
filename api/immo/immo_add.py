from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

add = Blueprint('immo_add', __name__)

@add.route("/immo/add", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "add").json()
