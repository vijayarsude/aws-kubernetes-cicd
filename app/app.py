import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Project 3 - Kubernetes CI/CD",
        "version": os.getenv("APP_VERSION", "1.0"),
        "hostname": os.getenv("HOSTNAME", "unknown")
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)