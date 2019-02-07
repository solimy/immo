from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

list = Blueprint('immo_list', __name__)

@list.route("/immo/list", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "list").json()
