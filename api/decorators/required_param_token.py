from functools import wraps
from flask import g, request, redirect, url_for
from ResponseObject import ResponseObject
import api
import db
import sqlite3 as sql

def required_param_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            if not api.TOKEN in request.json:
                return ResponseObject(api.ERROR, "missing param \""+ api.TOKEN +"\"").json()
            try:
                token = request.json[api.TOKEN]
                with sql.connect(db.DB) as con:
                    cur = con.cursor()
                    cur.execute("SELECT "+db.TOKEN+" FROM "+db.USERS+" WHERE "+db.TOKEN+"=?", (token,))
                    if cur.fetchone() is None:
                        return ResponseObject(api.ERROR, api.BAD_CREDENTIALS).json()
                    con.commit()
            except Exception as e:
                print(e)
                status = api.ERROR
                response = None
                con.rollback()

            finally:
                con.close()
        return f(*args, **kwargs)
    return decorated_function
