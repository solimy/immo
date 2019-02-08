from functools import wraps
from flask import g, request, redirect, url_for
from ResponseObject import ResponseObject
import api

def required_param_title(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            if not api.TITLE in request.json:
                return ResponseObject(api.ERROR, "missing param \""+ api.TITLE +"\"").json()
        return f(*args, **kwargs)
    return decorated_function
