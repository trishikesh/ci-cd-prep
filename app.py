from flask import Flask, request
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    env = os.getenv("ENVIRONMENT", "unknown")
    return f"Fixed the monitor report - {env}"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)
    return {"status": "received"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)