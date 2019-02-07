from flask import Blueprint, jsonify, request
from ResponseObject import ResponseObject
import decorators
import secrets
import api
import db
from passlib.hash import sha256_crypt
import sqlite3 as sql
import uuid

auth = Blueprint('user_auth', __name__)

@auth.route("/user/auth", methods = ["POST"])
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
                cur.execute("SELECT "+db.LOGIN+", "+db.PASSWORD_HASH+" FROM "+db.USERS+" WHERE "+db.LOGIN+"=?", (login,))
                fetched = cur.fetchone()
                if fetched is None:
                    status = api.ERROR
                    response = api.BAD_CREDENTIALS
                    return
                f_login, f_password_hash = fetched
                if not sha256_crypt.verify(password, f_password_hash):
                    status = api.ERROR
                    response = api.BAD_CREDENTIALS
                    return
                token = secrets.token_urlsafe()
                response = {api.TOKEN:token}
                cur.execute("UPDATE "+db.USERS+" SET "+db.TOKEN+" = ? WHERE "+db.LOGIN+" =?", (token,login,))
                con.commit()

        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()