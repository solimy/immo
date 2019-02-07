from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

immo_details = Blueprint('immo_details', __name__)

@immo_details.route("/immo/details", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "immo_details").json()
