from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import api
import db
import sqlite3 as sql

get = Blueprint('immo_get', __name__)

@get.route("/immo/get", methods = ["POST"])
@decorators.debug_request_display
@decorators.required_param_token
def handle():
    if request.method == "POST":
        status = api.SUCCESS
        response = None
        try:
            token = request.json[api.TOKEN]
            title = request.json[api.TITLE]
            with sql.connect(db.DB) as con:
                cur = con.cursor()
                cur.execute("SELECT "+db.LOGIN+", "+ db.TITLE+", "+db.NB_ROOMS+" FROM "+db.IMMOS+" WHERE "+db.TITLE+"=?", (title,))
                immo = cur.fetchone()
                if immo is None:
                    status = api.ERROR
                    response = api.IMMO_DONT_EXIST
                    return
                immo_login, immo_title, immo_nb_rooms = immo
                response = {api.LOGIN:immo_login, api.TITLE:immo_title, api.NB_ROOMS:immo_nb_rooms}
        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()