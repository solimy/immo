import sys
sys.path.append('api/')
from flask import Flask, jsonify
from register import register
from auth import auth

app = Flask(__name__)

app.register_blueprint(register, url_prefix="")
app.register_blueprint(auth, url_prefix="")

if __name__ == "__main__":
    app.run()
