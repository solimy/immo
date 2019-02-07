import sys
sys.path.append('api/')
from flask import Flask, jsonify
import api

app = Flask(__name__)

app.register_blueprint(api.register, url_prefix="")
app.register_blueprint(api.auth, url_prefix="")
app.register_blueprint(api.disconnect, url_prefix="")
app.register_blueprint(api.immo_add, url_prefix="")
app.register_blueprint(api.immo_list, url_prefix="")
app.register_blueprint(api.immo_details, url_prefix="")
app.register_blueprint(api.immo_edit, url_prefix="")
app.register_blueprint(api.immo_remove, url_prefix="")

if __name__ == "__main__":
    app.run()
