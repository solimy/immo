from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

remove = Blueprint('immo_remove', __name__)

@remove.route("/immo/remove", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "remove").json()
