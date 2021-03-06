from functools import wraps
from flask import g, request, redirect, url_for
from ResponseObject import ResponseObject
import api

def required_param_first_name(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            if not api.FIRST_NAME in request.json:
                return ResponseObject(api.ERROR, "missing param \""+ api.FIRST_NAME +"\"").json()
        return f(*args, **kwargs)
    return decorated_function
