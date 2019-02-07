from functools import wraps
from flask import g, request, redirect, url_for

def test(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            print("POST")
        if request.method == "GET":
            print("GET")
        #if g.user is None:
        #    return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
