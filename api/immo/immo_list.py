from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import api
import db
import sqlite3 as sql

list = Blueprint('immo_list', __name__)

@list.route("/immo/list", methods = ["POST"])
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
                cur.execute("SELECT "+ db.TITLE+" FROM "+db.IMMOS)
                immos = cur.fetchall()
                response = {api.TITLE:[*map(lambda immo: immo[0], immos)]}
        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()