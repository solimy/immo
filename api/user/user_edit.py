from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import api
import db
import sqlite3 as sql

edit = Blueprint('user_edit', __name__)

@edit.route("/user/edit", methods = ["POST"])
@decorators.debug_request_display
@decorators.required_param_first_name
@decorators.required_param_last_name
@decorators.required_param_birth_date
@decorators.required_param_token
def handle():
    if request.method == "POST":
        status = api.SUCCESS
        response = None
        try:
            token = request.json[api.TOKEN]
            with sql.connect(db.DB) as con:
                cur = con.cursor()
                cur.execute("UPDATE "+db.USERS+" SET "+db.LAST_NAME+"=?, "+db.FIRST_NAME+"=?, "+db.BIRTH_DATE+"=? WHERE "+db.TOKEN+" =?", (request.json[api.LAST_NAME],request.json[api.FIRST_NAME],request.json[api.BIRTH_DATE],request.json[api.TOKEN]))
        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()