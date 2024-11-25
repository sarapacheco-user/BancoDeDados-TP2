from flask import Flask, Blueprint, render_template, request, redirect
from connection import get_db_connection
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# Apply CORS globally for all routes
CORS(app, resources={r"/*": {
    "origins": "http://127.0.0.1:5500",  # Allow requests from this origin
    "methods": ["POST", "OPTIONS"],  # Allow specific methods
    "allow_headers": ["Content-Type"]  # Allow specific headers
}})

# Define the Blueprint for "fornecedores" (suppliers) routes
fornecedores_bp = Blueprint('fornecedores', __name__)

# Route to display all suppliers (GET method)
@fornecedores_bp.route("/")
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Fornecedor")
    fornecedores = cursor.fetchall()
    db.close()
    return render_template("fornecedores.html", fornecedores=fornecedores)

# Route to add a new supplier (POST method)
@fornecedores_bp.route("/adicionar_fornecedor", methods=["POST"])
def adicionar_fornecedor():
    db = get_db_connection()
    cursor = db.cursor()
    dados = request.form

    query = """
        INSERT INTO Fornecedor (nome_do_fornecedor, cidade, bairro, lote, cep)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (
        dados["nome_do_fornecedor"],
        dados["cidade"],
        dados["bairro"],
        dados["lote"],
        dados["cep"]
    )

    cursor.execute(query, valores)
    db.commit()
    db.close()

    return redirect("/fornecedores")
