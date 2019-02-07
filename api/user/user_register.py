from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators
import secrets
import api
import db
from passlib.hash import sha256_crypt
import sqlite3 as sql
import uuid

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
                    response = "user already exists"
                cur.execute("INSERT INTO "+db.USERS+"("+db.USER_UUID+", "+db.LOGIN+","+db.PASSWORD_HASH+") VALUES(?, ?, ?)", (str(uuid.uuid4()), login, sha256_crypt.encrypt(password)))
                con.commit()

        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()
