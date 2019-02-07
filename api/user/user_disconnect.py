from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import secrets
import api
import db
from passlib.hash import sha256_crypt
import sqlite3 as sql

disconnect = Blueprint('user_disconnect', __name__)

@disconnect.route("/user/disconnect", methods = ["POST"])
@decorators.debug_request_display
@decorators.required_param_token
def handle():
    if request.method == "POST":
        status = api.SUCCESS
        response = None
        try:
            token = request.json[api.TOKEN]
            with sql.connect(db.DB) as con:
                cur = con.cursor()
                cur.execute("UPDATE "+db.USERS+" SET "+db.TOKEN+" = ? WHERE "+db.TOKEN+" =?", ("",token,))
                con.commit()
                print("ho ho ho")
        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()