from functools import wraps
from flask import g, request, redirect, url_for

def debug_request_display(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(request)
        #if g.user is None:
        #    return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
