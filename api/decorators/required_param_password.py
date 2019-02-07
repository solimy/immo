from functools import wraps
from flask import g, request, redirect, url_for
from ResponseObject import ResponseObject


def required_param_password(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            print("POST")
        if not "password" in request.json:
            return ResponseObject(101, "missing param \"password\"").json()
        if request.method == "GET":
            print("GET")
        #if g.user is None:
        #    return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
