from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject

register = Blueprint('register', __name__)

@register.route("/register", methods = ["GET", "POST"])
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "register").json()
