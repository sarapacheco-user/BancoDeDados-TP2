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

# Define the Blueprint for "funcionarios" routes
funcionarios_bp = Blueprint("funcionarios", __name__)

@funcionarios_bp.route("/adicionar_funcionario", methods=["POST"])
def adicionar_funcionario():
    db = get_db_connection()

    if db is None:
        return "Erro ao conectar ao banco de dados.", 500
    
    cursor = db.cursor()
    dados = request.form

    query = """
        INSERT INTO Funcionario (nome, sobrenome, sede_id, salario, departamento, data_nascimento, data_admissao, cargo, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        dados["nome"],
        dados["sobrenome"],
        dados["sede_id"],
        dados["salario"],
        dados["departamento"],
        dados["data_nascimento"],
        dados["data_admissao"],
        dados["cargo"],
        dados["email"]
    )

    try:
        # Execute the query and commit the changes
        cursor.execute(query, valores)
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return f"Erro ao adicionar funcionário: {e}", 500
    finally:
        db.close()

    return redirect("/funcionarios")
