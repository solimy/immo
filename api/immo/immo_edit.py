from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import api
import db
import sqlite3 as sql

edit = Blueprint('immo_edit', __name__)

@edit.route("/immo/edit", methods = ["POST"])
@decorators.debug_request_display
@decorators.required_param_title
@decorators.required_param_nb_rooms
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
                cur.execute("SELECT "+db.LOGIN+", "+ db.TITLE+" FROM "+db.IMMOS+" WHERE "+db.TITLE+"=?", (title,))
                immo = cur.fetchone()
                if immo is None:
                    status = api.ERROR
                    response = api.IMMO_DONT_EXIST
                    return
                immo_login, immo_title = immo
                if cur.execute("SELECT "+db.LOGIN+" FROM "+db.USERS+" WHERE "+db.TOKEN+"=?", (token,)).fetchone()[0] != immo_login:
                    status = api.ERROR
                    response = api.NOT_IMMO_OWNER
                    return
                cur.execute("UPDATE "+db.IMMOS+" SET "+db.NB_ROOMS+"=? WHERE "+db.TITLE+"=?", (request.json[api.NB_ROOMS], title,))
                con.commit()
        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()