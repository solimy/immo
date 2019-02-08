from flask import Blueprint, request
from ResponseObject import ResponseObject
import decorators
import secrets
import api
import db
import sqlite3 as sql

add = Blueprint('immo_add', __name__)

@add.route("/immo/add", methods = ["POST"])
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
                cur.execute("SELECT "+db.TITLE+" FROM "+db.IMMOS+" WHERE "+db.TITLE+"=?", (title,))
                if not cur.fetchone() is None:
                    status = api.ERROR
                    response = api.IMMO_ALREADY_EXIST
                    return
                cur.execute("SELECT "+db.LOGIN+" FROM "+db.USERS+" WHERE "+db.TOKEN+"=?", (token,))
                login = cur.fetchone()[0]
                cur.execute("INSERT INTO "+db.IMMOS+" ("+db.LOGIN+", "+db.TITLE+", "+db.NB_ROOMS+") VALUES (?, ?, ?)", (login, request.json[api.TITLE], request.json[api.NB_ROOMS]))
                con.commit()
        except Exception as e:
            print(e)
            status = api.ERROR
            response = None
            con.rollback()

        finally:
            return ResponseObject(status, response).json()
            con.close()