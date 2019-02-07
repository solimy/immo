import sys
sys.path.append('api/')
from flask import Flask, jsonify
import api

app = Flask(__name__)

app.register_blueprint(api.user.register, url_prefix="")
app.register_blueprint(api.user.auth, url_prefix="")
app.register_blueprint(api.user.disconnect, url_prefix="")
app.register_blueprint(api.user.get, url_prefix="")
app.register_blueprint(api.user.edit, url_prefix="")
app.register_blueprint(api.immo.add, url_prefix="")
app.register_blueprint(api.immo.list, url_prefix="")
app.register_blueprint(api.immo.get, url_prefix="")
app.register_blueprint(api.immo.edit, url_prefix="")
app.register_blueprint(api.immo.remove, url_prefix="")

if __name__ == "__main__":
    app.run()
