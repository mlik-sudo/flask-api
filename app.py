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
import docx
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcul', methods=['GET'])
def getMaxPages():
    # Code existant pour calculer le nombre de pages
    return jsonify({"max_pages": 42})  # Exemple

def extract_problematic(doc_path):
    """
    Scanne un document DOCX et extrait la problématique si elle est détectée.
    Sinon, propose une reformulation basée sur le contenu.
    """
    try:
        doc = docx.Document(doc_path)
        keywords = ["problématique", "question de recherche", "objectif de l'étude", "cette recherche s'intéresse à", "cette étude vise à"]
        
        for para in doc.paragraphs:
            for keyword in keywords:
                if keyword.lower() in para.text.lower():
                    return f"🔍 Problématique détectée : {para.text}"

        return "⚠️ Problématique exacte non trouvée. Voulez-vous une reformulation basée sur le contenu ?"

    except Exception as e:
        return f"❌ Erreur lors de la lecture du document : {e}"

@app.route('/detect_problematic', methods=['POST'])
def detect_problematic():
    """
    Endpoint pour détecter la problématique dans un document DOCX.
    """
    if 'file' not in request.files:
        return jsonify({"error": "Aucun fichier reçu"}), 400
    
    file = request.files['file']
    file_path = "temp.docx"
    file.save(file_path)

    problematic_text = extract_problematic(file_path)
    response = {"problematique": problematic_text}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # On force Flask à utiliser le port 5001
    app.run(host="0.0.0.0", port=port)

