from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from connection import get_db_connection

# Initialize Flask app
app = Flask(__name__)

# Apply CORS globally for specific routes
CORS(app, resources={r"/*": {
    "origins": "http://127.0.0.1:5500",
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type"]
}})

# Route to display fornecedores (GET method)
@app.route("/fornecedores")
def fornecedores():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Fornecedor")
    fornecedores = cursor.fetchall()
    db.close()
    return render_template("fornecedores.html", fornecedores=fornecedores)

# Route to add a new fornecedor (POST method)
@app.route("/fornecedores/adicionar_fornecedor", methods=["POST"])
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

# Route to display clientes (GET method)
@app.route("/clientes")
def clientes():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ClienteCadastrado")
    clientes = cursor.fetchall()
    db.close()
    return render_template("clientes.html", clientes=clientes)

# Route to add a new cliente (POST method)
@app.route("/clientes/adicionar_cliente", methods=["POST"])
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

# Route to display pedidos (GET method)
@app.route("/pedidos")
def pedidos():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Pedido")
    pedidos = cursor.fetchall()
    db.close()
    return render_template("pedidos.html", pedidos=pedidos)

# Route to add a new pedido (POST method)
@app.route("/pedidos/adicionar_pedido", methods=["POST"])
def adicionar_pedido():
    db = get_db_connection()
    cursor = db.cursor()

    dados = request.form
    cliente_id = dados["cliente_id"]
    sede_id = dados["sede_id"]
    funcionario_que_auxiliou_id = dados["funcionario_que_auxiliou_id"]

    query = """
        INSERT INTO Pedido (cliente_id, sede_id, funcionario_que_auxiliou_id)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (cliente_id, sede_id, funcionario_que_auxiliou_id))
    pedido_id = cursor.lastrowid

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

    return redirect("/pedidos")

# Route to display produtos (GET method)
@app.route("/produtos")
def produtos():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Produto")
    produtos = cursor.fetchall()
    db.close()
    return render_template("produtos.html", produtos=produtos)

# Route to add a new produto (POST method)
@app.route("/produtos/adicionar_produto", methods=["POST"])
def adicionar_produto():
    db = get_db_connection()
    cursor = db.cursor()
    dados = request.form

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

    cursor.execute(query, valores)
    db.commit()
    db.close()

    return redirect("/produtos/")

# Route to display sedes (GET method)
@app.route("/sedes")
def sedes():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sede")
    sedes = cursor.fetchall()
    db.close()
    return render_template("sedes.html", sedes=sedes)

# Route to add a new sede (POST method)
@app.route("/sedes/adicionar_sede", methods=["POST"])
def adicionar_sede():
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

    return redirect("/sedes")

# Main entry point to run the application
if __name__ == "__main__":
    app.run(debug=True)
