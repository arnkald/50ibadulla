import os
import requests
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

import os

TELEGRAM_BOT_TOKEN = os.environ.get("8795557460:AAEePwZfZ7nkm3FId0d7CojBr25Xtldv9to")
CHAT_ID = os.environ.get("919183343")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/music.mp3")
def music():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), "static/music.mp3")


@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    name = data.get("name", "").strip()
    status = data.get("status", "").strip()

    if not name or not status:
        return jsonify({"ok": False, "error": "Missing fields"}), 400

    message = (
        f"🎉 Жаңа жауап!\n\n"
        f"👤 Аты: {name}\n"
        f"📝 Жауабы: {status}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, json={"chat_id": CHAT_ID, "text": message}, timeout=10)
        return jsonify({"ok": resp.ok})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)