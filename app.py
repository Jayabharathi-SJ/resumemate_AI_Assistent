import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Please enter a message."})

    # Demo response. Add your preferred AI API here later.
    reply = (
        "ResumeMate AI Assistant is ready! "
        "I can help you improve your resume, write a professional summary, "
        "suggest skills, and prepare interview questions."
    )
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
