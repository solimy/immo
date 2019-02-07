from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

auth = Blueprint('auth', __name__)

@auth.route("/auth", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "auth").json()
