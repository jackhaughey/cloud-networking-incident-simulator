from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "service": "app1",
        "host": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
