from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API Flask est en ligne ! 🚀"

@app.route("/calcul", methods=["GET"])
def calcul():
    """ Route pour calculer le découpage optimal. """
    C = float(request.args.get("C", 10000))
    F = float(request.args.get("F", 0.7))
    W = float(request.args.get("W", 450))
    S = float(request.args.get("S", 1.6))
    I = float(request.args.get("I", 1))

    max_tokens = C * (1 - F)
    tokens_per_page = (W * S) + (I * 0.5)
    max_pages = max(1, round(max_tokens / tokens_per_page))

    return jsonify({"max_pages": max_pages})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # On force Flask à utiliser le port 5001
    app.run(host="0.0.0.0", port=port)

