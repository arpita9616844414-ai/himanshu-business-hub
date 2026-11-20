
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip().lower()

    if not question:
        return jsonify({"answer": "Please enter a question."})

    if "owner" in question or "himanshu" in question:
        answer = "Himanshu is the business owner."
    elif "partner" in question:
        answer = "Thank you for your interest in partnership!"
    elif "transport" in question:
        answer = "We focus on transportation and logistics."
    elif "manufacturing" in question:
        answer = "Please contact the owner for manufacturing details."
    else:
        answer = "Please contact Himanshu on WhatsApp for further assistance."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    