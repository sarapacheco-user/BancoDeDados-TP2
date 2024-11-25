from flask import Flask, Blueprint, render_template, request, redirect
from connection import get_db_connection
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# Apply CORS globally for all routes
CORS(app, resources={r"/*": {
    "origins": "http://127.0.0.1:5500",  # Allow requests from this origin
    "methods": ["GET", "POST", "OPTIONS"],  # Allow specific methods
    "allow_headers": ["Content-Type"]  # Allow specific headers
}})

# Test the database connection
try:
    db = get_db_connection()
    if db.is_connected():
        print("Conexão bem-sucedida!")
        db.close()
    else:
        print("Falha na conexão.")
except Exception as e:
    print(f"Erro: {e}")

# Define the Blueprint for "clientes" (clients) routes
clientes_bp = Blueprint('clientes', __name__)

# Route to display all clients (GET method)
@clientes_bp.route("/")
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ClienteCadastrado")
    clientes = cursor.fetchall()
    db.close()
    return render_template("clientes.html", clientes=clientes)

# Route to add a new client (POST method)
@clientes_bp.route("/adicionar_cliente", methods=["POST"])
def adicionar_cliente():
    db = get_db_connection()
    cursor = db.cursor()
    dados = request.form

    query = """
        INSERT INTO ClienteCadastrado (nome, sobrenome, data_nascimento, data_cadastro, cep, numero_endereco)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        dados["nome"],
        dados["sobrenome"],
        dados["data_nascimento"],
        dados["data_cadastro"],
        dados["cep"],
        dados["numero_endereco"]
    )

    cursor.execute(query, valores)
    db.commit()
    db.close()

    return redirect("/clientes")

# Register the Blueprint with the app
app.register_blueprint(clientes_bp, url_prefix="/clientes")

# Main entry point to run the application
if __name__ == "__main__":
    app.run(debug=True)
