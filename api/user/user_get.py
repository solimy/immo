from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import secrets
import api
import db
import sqlite3 as sql

get = Blueprint('user_get', __name__)

@get.route("/user/get", methods = ["POST"])
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
                cur.execute("SELECT "+db.LAST_NAME+", "+db.FIRST_NAME+", "+db.BIRTH_DATE+" FROM "+db.USERS+" WHERE "+db.TOKEN+" =?", (token,))
                last_name, first_name, birth_date = cur.fetchone()
                response = {api.LAST_NAME:last_name, api.FIRST_NAME:first_name, api.BIRTH_DATE:birth_date}
        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()