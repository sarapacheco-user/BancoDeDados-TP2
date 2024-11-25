from flask import Flask, render_template, request, redirect, Blueprint, url_for
import sys
import os
from flask_cors import CORS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection import get_db_connection

# Initialize the Flask app
app = Flask(__name__)

# Apply CORS globally
CORS(app, resources={r"/*": {
    "origins": "http://127.0.0.1:5500",
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type"]
}})

# Defining the Blueprint for "sedes" routes
sedes_bp = Blueprint("sedes", __name__)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# Route for displaying the sedes
@sedes_bp.route("/")
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sede")
    sedes = cursor.fetchall()
    db.close()
    return render_template("sedes.html", sedes=sedes)

# Route to add a new sede (GET and POST methods)
@sedes_bp.route("/adicionar_sede", methods=["GET", "POST"])
def adicionar_sede():
    if request.method == "POST":
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        lote = request.form["lote"]
        cep = request.form["cep"]

        db = get_db_connection()
        cursor = db.cursor()
        query = "INSERT INTO Sede (cidade, bairro, lote, cep) VALUES (%s, %s, %s, %s)"
        values = (cidade, bairro, lote, cep)
        cursor.execute(query, values)
        db.commit()
        db.close()

        return redirect(url_for("sedes.index"))

    return render_template("adicionar_sede.html")
# Register the Blueprint with a URL prefix
app.register_blueprint(sedes_bp, url_prefix="/sedes")

if __name__ == "__main__":
    app.run(debug=True)
