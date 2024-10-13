import pickle
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    string_data = request.json["data"]

    data = base64.b64decode(string_data.encode())
    pickle.loads(data)
    return jsonify(data="unpickled")

app.run(debug=True)
