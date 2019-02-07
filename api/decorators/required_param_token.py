from functools import wraps
from flask import g, request, redirect, url_for
from ResponseObject import ResponseObject
import api
import db
from passlib.hash import sha256_crypt
import sqlite3 as sql
def required_param_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            if not api.TOKEN in request.json:
                return ResponseObject(api.ERROR, "missing param \""+ api.TOKEN +"\"").json()
        return f(*args, **kwargs)
    return decorated_function




register = Blueprint('user_register', __name__)

@register.route("/user/register", methods = ["POST"])
@decorators.debug_request_display
@decorators.required_param_login
@decorators.required_param_password
def handle():
    if request.method == "POST":
        status = api.SUCCESS
        response = "response"       
        try:
            login = request.json[api.LOGIN]
            password = request.json[api.PASSWORD]
            with sql.connect(db.DB) as con:
                cur = con.cursor()
                cur.execute("SELECT "+db.LOGIN+" FROM "+db.USERS+" WHERE "+db.LOGIN+"=?", (login,))
                if not cur.fetchone() is None:
                    status = api.ERROR
                    response = api.USER_ALREADY_EXIST
                cur.execute("INSERT INTO "+db.USERS+"("+db.LOGIN+","+db.PASSWORD_HASH+") VALUES(?, ?)", (login, sha256_crypt.encrypt(password)))
                con.commit()

        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()
