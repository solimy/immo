from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

immo_list = Blueprint('immo_list', __name__)

@immo_list.route("/immo/list", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "immo_list").json()
