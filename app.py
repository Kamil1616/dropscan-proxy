from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

THERUNDOWN_BASE = "https://therundown.io/api/v2"

@app.route("/")
def home():
    return "DropScan Proxy calisıyor"

@app.route("/api/<path:endpoint>")
def proxy(endpoint):
    params = dict(request.args)
    url = f"{THERUNDOWN_BASE}/{endpoint}"
    try:
        r = requests.get(url, params=params, timeout=15)
        return Response(r.content, status=r.status_code, mimetype="application/json")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
