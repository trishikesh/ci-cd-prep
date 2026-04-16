from flask import Flask, request
import osssssss
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    env = os.getenv("ENVIRONMENT", "unknown")
    return f"I hope i can fix him - {env}"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)
    return {"status": "received"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)