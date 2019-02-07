import sqlite3
import db

conn = sqlite3.connect(db.DB)
print("Opened database successfully")

conn.execute("CREATE TABLE "+db.USERS+" ("+db.USER_UUID+" BLOB, "+db.LOGIN+" TEXT, "+db.PASSWORD_HASH+" BLOB, "+db.TOKEN+" TEXT, "+db.FIRST_NAME+" TEXT, "+db.LAST_NAME+" TEXT, "+db.BIRTH_DATE+" DATE)")
conn.execute("CREATE TABLE "+db.IMMOS+" ("+db.IMMO_UUID+" BLOB, "+db.USER_UUID+" BLOB, "+db.TITLE+" TEXT, "+db.NB_ROOMS+" INTEGER)")
print("Table created successfully")
conn.close()