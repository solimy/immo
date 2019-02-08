import sys
sys.path.append('api/')
import user
import immo

SUCCESS = "success"
ERROR = "error"

STATUS = "status"
LOGIN = "login"
PASSWORD = "password"
TOKEN = "token"
FIRST_NAME = "first_name" 
LAST_NAME = "last_name" 
BIRTH_DATE = "birth_date"
TITLE = "title" 
NB_ROOMS = "nb_rooms"

USER_ALREADY_EXIST = "user already exists"
IMMO_ALREADY_EXIST = "immo already exists"
IMMO_DONT_EXIST = "immo does not exist"
NOT_IMMO_OWNER = "you do not own this immo"
BAD_CREDENTIALS = "bad credentials"

