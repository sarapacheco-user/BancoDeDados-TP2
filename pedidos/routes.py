from flask import Flask, render_template, request, redirect, Blueprint
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

# Define the Blueprint for "pedidos" routes
pedidos_bp = Blueprint("pedidos", __name__)

# Route for displaying pedidos (GET method)
@pedidos_bp.route("/")
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Pedido")
    pedidos = cursor.fetchall()
    db.close()
    return render_template("pedidos.html", pedidos=pedidos)

# Route to add a new pedido (POST method)
@pedidos_bp.route("/adicionar_pedido", methods=["POST"])
def adicionar_pedido():
    db = get_db_connection()
    cursor = db.cursor()

    # Get form data
    dados = request.form
    cliente_id = dados["cliente_id"]
    sede_id = dados["sede_id"]
    funcionario_que_auxiliou_id = dados["funcionario_que_auxiliou_id"]

    # Insert into Pedido table
    query = """
        INSERT INTO Pedido (cliente_id, sede_id, funcionario_que_auxiliou_id)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (cliente_id, sede_id, funcionario_que_auxiliou_id))
    pedido_id = cursor.lastrowid  # Get the last inserted pedido ID

    # Insert associated products into Pedido_Produto table
    produto_ids = dados.getlist("produto_id[]")
    quantidades = dados.getlist("quantidade[]")

    for produto_id, quantidade in zip(produto_ids, quantidades):
        query_produto = """
            INSERT INTO Pedido_Produto (pedido_id, produto_id, quantidade)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query_produto, (pedido_id, produto_id, quantidade))

    db.commit()
    db.close()

    return redirect("/")

# Register the Blueprint with the app
app.register_blueprint(pedidos_bp, url_prefix="/pedidos")

# Main entry point to run the application
if __name__ == "__main__":
    app.run(debug=True)
