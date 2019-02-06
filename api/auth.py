from flask import Blueprint, jsonify
from ResponseObject import ResponseObject

auth = Blueprint('auth', __name__)

@auth.route("/auth")
def accountList():
    return ResponseObject(400, "auth").json()
