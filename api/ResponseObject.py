from flask import jsonify

class ResponseObject:
    def __init__(self, status, response):
        self.status = status
        self.response = response

    def json(self):
        return jsonify({"status":self.status, "response":self.response})
