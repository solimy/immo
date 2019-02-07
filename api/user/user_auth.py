from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators

auth = Blueprint('user_auth', __name__)

@auth.route("/user/auth", methods = ["GET", "POST"])
@decorators.test
def handle():
    if request.method == "POST":
        return ResponseObject(500, {})
    if request.method == "GET":
        return ResponseObject(400, "auth").json()
