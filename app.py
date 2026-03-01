import os
import requests
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8795557460:AAEePwZfZ7nkm3FId0d7CojBr25Xtldv9to"
CHAT_ID            = "919183343"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/music.mp3")
def music():
    return send_from_directory(
        os.path.join(app.root_path, "static"), "music.mp3"
    )

@app.route("/send", methods=["POST"])
def send():
    data   = request.get_json(silent=True) or {}
    name   = data.get("name",   "").strip()
    status = data.get("status", "").strip()

    if not name or not status:
        return jsonify({"ok": False, "error": "Missing fields"}), 400

    message = (
        f"🎉 Жаңа жауап!\n\n"
        f"👤 Аты: {name}\n"
        f"📝 Жауабы: {status}\n\n"
        f"━━━━━━━━━━━━━━━━\n"
        f"📅 28 наурыз 2026 жыл\n"
        f"🕕 18:00\n"
        f"🏛 Керуен Сарайы, Шымкент"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp   = requests.post(url, json={"chat_id": CHAT_ID, "text": message}, timeout=10)
        result = resp.json()
        if not result.get("ok"):
            return jsonify({"ok": False, "error": result.get("description")}), 400
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
```

Төменде **"Commit changes"** батырмасын басыңыз ✅

---

## 3-ҚАДАМ: Chat ID алыңыз

Браузерде мына сілтемені ашыңыз:
```
https://api.telegram.org/bot8795557460:AAEePojBr25Xtldv9to/getUpdates
