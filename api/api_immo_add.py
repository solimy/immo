from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

immo_add = Blueprint('immo_add', __name__)

@immo_add.route("/immo/add", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "immo_add").json()
