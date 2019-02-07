import sys
sys.path.append('api/')
from flask import Flask, jsonify
from api_register import register
from api_auth import auth
from api_disconnect import disconnect
from api_immo_add import immo_add
from api_immo_list import immo_list
from api_immo_details import immo_details
from api_immo_edit import immo_edit
from api_immo_remove import immo_remove
