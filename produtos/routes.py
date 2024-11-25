from flask import Flask, render_template, request, redirect, Blueprint
from connection import get_db_connection
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Apply CORS globally for specific routes
CORS(app, resources={r"/*": {
    "origins": "http://127.0.0.1:5500",  # Allow requests from this origin
    "methods": ["POST", "OPTIONS"],  # Allow specific methods
    "allow_headers": ["Content-Type"]  # Allow specific headers
}})

# Define the Blueprint for "produtos" routes
produtos_bp = Blueprint("produtos", __name__)

# Route for displaying produtos (GET method)
@produtos_bp.route("/")
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Produto")
    produtos = cursor.fetchall()
    db.close()
    return render_template("produtos.html", produtos=produtos)

# Route to add a new produto (POST method)
@produtos_bp.route("/adicionar_produto", methods=["POST"])
def adicionar_produto():
    db = get_db_connection()
    cursor = db.cursor()
    dados = request.form

    # Define the insert query for Produto table
    query = """
        INSERT INTO Produto (
            tipo_de_peca, fornecedor_id, custo_aquisicao, custo_marketing, 
            margem_de_lucro, preco_de_venda, despesas, q_em_estoque
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        dados["tipo_de_peca"],
        dados["fornecedor_id"],
        dados["custo_aquisicao"],
        dados["custo_marketing"],
        dados["margem_de_lucro"],
        dados["preco_de_venda"],
        dados["despesas"],
        dados["q_em_estoque"]
    )

    # Execute the query to insert the produto
    cursor.execute(query, valores)
    db.commit()
    db.close()

    # Redirect to the produtos page
    return redirect("/produtos/")


# Register the Blueprint with the app
app.register_blueprint(produtos_bp, url_prefix="/produtos")

# Main entry point to run the application
if __name__ == "__main__":
    app.run(debug=True)
