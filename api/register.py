from flask import Blueprint, jsonify
from ResponseObject import ResponseObject

register = Blueprint('register', __name__)

@register.route("/register")
def accountList():
    return ResponseObject(400, "register").json()
