from functools import wraps
from flask import g, request, redirect, url_for
from ResponseObject import ResponseObject
import api

def required_param_nb_rooms(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            if not api.NB_ROOMS in request.json:
                return ResponseObject(api.ERROR, "missing param \""+ api.NB_ROOMS +"\"").json()
        return f(*args, **kwargs)
    return decorated_function
