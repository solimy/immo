from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import api
import db
from passlib.hash import sha256_crypt
import sqlite3 as sql

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
