import streamlit as st
import mysql.connector

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # ou o host do seu banco
        user="teste15",    # seu usuário
        password="senha",  # sua senha
        database="lojaderoupas"  # nome do banco de dados
    )

# Função para exibir fornecedores
def mostrar_fornecedores():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Fornecedor")
    fornecedores = cursor.fetchall()
    db.close()

    st.write("### Fornecedores")
    for fornecedor in fornecedores:
        st.write(f"Nome: {fornecedor['nome_do_fornecedor']}, Cidade: {fornecedor['cidade']}, Bairro: {fornecedor['bairro']}")

# Função para adicionar fornecedor
def adicionar_fornecedor():
    st.subheader("Adicionar Fornecedor")
    nome_do_fornecedor = st.text_input("Nome do Fornecedor")
    cidade = st.text_input("Cidade")
    bairro = st.text_input("Bairro")
    lote = st.text_input("Lote")
    cep = st.text_input("CEP")

    if st.button("Adicionar Fornecedor"):
        if nome_do_fornecedor and cidade and bairro and lote and cep:
            db = get_db_connection()
            cursor = db.cursor()
            query = """
                INSERT INTO Fornecedor (nome_do_fornecedor, cidade, bairro, lote, cep)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nome_do_fornecedor, cidade, bairro, lote, cep))
            db.commit()
            db.close()
            st.success("Fornecedor adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

# Função para exibir clientes
def mostrar_clientes():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ClienteCadastrado")
    clientes = cursor.fetchall()
    db.close()

    st.write("### Clientes")
    for cliente in clientes:
        st.write(f"Nome: {cliente['nome']}, Sobrenome: {cliente['sobrenome']}, CEP: {cliente['cep']}")

# Função para adicionar cliente
def adicionar_cliente():
    st.subheader("Adicionar Cliente")
    nome = st.text_input("Nome")
    sobrenome = st.text_input("Sobrenome")
    data_nascimento = st.date_input("Data de Nascimento")
    data_cadastro = st.date_input("Data de Cadastro")
    cep = st.text_input("CEP")
    numero_endereco = st.text_input("Número do Endereço")

    if st.button("Adicionar Cliente"):
        if nome and sobrenome and data_nascimento and data_cadastro and cep and numero_endereco:
            db = get_db_connection()
            cursor = db.cursor()
            query = """
                INSERT INTO ClienteCadastrado (nome, sobrenome, data_nascimento, data_cadastro, cep, numero_endereco)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nome, sobrenome, data_nascimento, data_cadastro, cep, numero_endereco))
            db.commit()
            db.close()
            st.success("Cliente adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

# Função para exibir produtos
def mostrar_produtos():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Produto")
    produtos = cursor.fetchall()
    db.close()

    st.write("### Produtos")
    for produto in produtos:
        st.write(f"Tipo de Peça: {produto['tipo_de_peca']}, Preço: {produto['preco_de_venda']}, Estoque: {produto['q_em_estoque']}")

# Função para adicionar produto
def adicionar_produto():
    st.subheader("Adicionar Produto")
    tipo_de_peca = st.text_input("Tipo de Peça")
    fornecedor_id = st.text_input("ID do Fornecedor")
    custo_aquisicao = st.number_input("Custo de Aquisição", min_value=0.0)
    preco_de_venda = st.number_input("Preço de Venda", min_value=0.0)
    q_em_estoque = st.number_input("Quantidade em Estoque", min_value=0)

    if st.button("Adicionar Produto"):
        if tipo_de_peca and fornecedor_id and custo_aquisicao and preco_de_venda and q_em_estoque:
            db = get_db_connection()
            cursor = db.cursor()
            query = """
                INSERT INTO Produto (tipo_de_peca, fornecedor_id, custo_aquisicao, preco_de_venda, q_em_estoque)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (tipo_de_peca, fornecedor_id, custo_aquisicao, preco_de_venda, q_em_estoque))
            db.commit()
            db.close()
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
def mostrar_funcionarios():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Funcionario")
    funcionarios = cursor.fetchall()
    db.close()

    st.write("### Funcionários")
    for funcionario in funcionarios:
        st.write(f"Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Sede: {funcionario['sede_id']}")

# Função para adicionar funcionário
def adicionar_funcionario():
    st.subheader("Adicionar Funcionário")
    nome = st.text_input("Nome")
    cargo = st.text_input("Cargo")
    sede_id = st.text_input("ID da Sede")
    data_admissao = st.date_input("Data de Admissão")
    salario = st.number_input("Salário", min_value=0.0)

    if st.button("Adicionar Funcionário"):
        if nome and cargo and sede_id and data_admissao and salario:
            db = get_db_connection()
            cursor = db.cursor()
            query = """
                INSERT INTO Funcionario (nome, cargo, sede_id, data_admissao, salario)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nome, cargo, sede_id, data_admissao, salario))
            db.commit()
            db.close()
            st.success("Funcionário adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
# Função para exibir sedes
def mostrar_sedes():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sede")
    sedes = cursor.fetchall()
    db.close()

    st.write("### Sedes")
    for sede in sedes:
        st.write(f"Cidade: {sede['cidade']}, Bairro: {sede['bairro']}, Lote: {sede['lote']}, CEP: {sede['cep']}")

# Função para adicionar sede
def adicionar_sede():
    st.subheader("Adicionar Sede")
    cidade = st.text_input("Cidade")
    bairro = st.text_input("Bairro")
    lote = st.text_input("Lote")
    cep = st.text_input("CEP")

    if st.button("Adicionar Sede"):
        if cidade and bairro and lote and cep:
            db = get_db_connection()
            cursor = db.cursor()
            query = """
                INSERT INTO Sede (cidade, bairro, lote, cep)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (cidade, bairro, lote, cep))
            db.commit()
            db.close()
            st.success("Sede adicionada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
# Função para exibir pedidos
def mostrar_pedidos():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Pedido")
    pedidos = cursor.fetchall()
    db.close()

    st.write("### Pedidos")
    for pedido in pedidos:
        st.write(f"ID do Pedido: {pedido['id']}, Cliente ID: {pedido['cliente_id']}, Sede ID: {pedido['sede_id']}, Funcionário: {pedido['funcionario_que_auxiliou_id']}")

# Função para adicionar pedido
def adicionar_pedido():
    st.subheader("Adicionar Pedido")
    cliente_id = st.text_input("ID do Cliente")
    sede_id = st.text_input("ID da Sede")
    funcionario_que_auxiliou_id = st.text_input("ID do Funcionário que Auxiliou")
    
    produtos = []
    quantidade_produtos = []

    with st.expander("Adicionar Produtos ao Pedido"):
        num_produtos = st.number_input("Número de Produtos", min_value=1, max_value=10, value=1)
        
        for i in range(num_produtos):
            st.write(f"Produto {i+1}")
            produto_id = st.text_input(f"ID do Produto {i+1}")
            quantidade = st.number_input(f"Quantidade do Produto {i+1}", min_value=1, value=1)
            produtos.append(produto_id)
            quantidade_produtos.append(quantidade)

    if st.button("Adicionar Pedido"):
        if cliente_id and sede_id and funcionario_que_auxiliou_id and produtos:
            db = get_db_connection()
            cursor = db.cursor()
            query = """
                INSERT INTO Pedido (cliente_id, sede_id, funcionario_que_auxiliou_id)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (cliente_id, sede_id, funcionario_que_auxiliou_id))
            pedido_id = cursor.lastrowid  # Obtém o ID do pedido inserido

            # Insere os produtos associados ao pedido
            for produto_id, quantidade in zip(produtos, quantidade_produtos):
                query_produto = """
                    INSERT INTO Pedido_Produto (pedido_id, produto_id, quantidade)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query_produto, (pedido_id, produto_id, quantidade))

            db.commit()
            db.close()
            st.success("Pedido adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
# Função para gerar filtros dinâmicos para qualquer tabela
def aplicar_filtros(tabela, filtros, colunas_selecionadas):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    # Construção da cláusula WHERE com base nos filtros fornecidos
    where_clauses = []
    params = []
    
    for coluna, valor in filtros.items():
        if isinstance(valor, tuple) and len(valor) == 2:  # Caso seja um intervalo
            where_clauses.append(f"{coluna} BETWEEN %s AND %s")
            params.extend(valor)
        elif valor:  # Filtro simples (não vazio ou None)
            where_clauses.append(f"{coluna} LIKE %s")
            params.append(f"%{valor}%")
    
    where_query = " AND ".join(where_clauses)
    if where_query:
        where_query = "WHERE " + where_query

    colunas = ", ".join(colunas_selecionadas) if colunas_selecionadas else "*"
    query = f"SELECT {colunas} FROM {tabela} {where_query}"
    
    cursor.execute(query, tuple(params))
    resultados = cursor.fetchall()
    db.close()
    return resultados

def mostrar_fornecedores_com_filtro():
    st.subheader("Filtrar Fornecedores")

    # Inputs para filtros dinâmicos para fornecedores
    nome_fornecedor = st.text_input("Nome do Fornecedor")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    
    # Filtro para a quantidade de produtos fornecidos ou outro critério
    produtos_min = st.number_input("Número mínimo de Produtos Fornecidos", min_value=0, value=0)
    produtos_max = st.number_input("Número máximo de Produtos Fornecidos", min_value=0, value=1000)
    
    if st.button("Filtrar Fornecedores"):
        filtros = {}

        if nome_fornecedor:
            filtros["nome_fornecedor"] = nome_fornecedor
        if cidade:
            filtros["cidade"] = cidade
        if estado:
            filtros["estado"] = estado
        if produtos_min is not None and produtos_max is not None:
            filtros["numero_de_produtos"] = (produtos_min, produtos_max)

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        # Construção da consulta dinâmica com base nos filtros
        where_clauses = []
        params = []

        if "nome_fornecedor" in filtros:
            where_clauses.append("nome_fornecedor LIKE %s")
            params.append(f"%{filtros['nome_fornecedor']}%")
        
        if "cidade" in filtros:
            where_clauses.append("cidade LIKE %s")
            params.append(f"%{filtros['cidade']}%")
        
        if "estado" in filtros:
            where_clauses.append("estado LIKE %s")
            params.append(f"%{filtros['estado']}%")
        
        if "numero_de_produtos" in filtros:
            where_clauses.append("numero_de_produtos BETWEEN %s AND %s")
            params.extend(filtros["numero_de_produtos"])

        where_query = " AND ".join(where_clauses)
        if where_query:
            where_query = "WHERE " + where_query

        query = f"SELECT * FROM Fornecedor {where_query}"

        cursor.execute(query, tuple(params))
        fornecedores = cursor.fetchall()
        db.close()

        st.write("### Fornecedores Filtrados")
        if fornecedores:
            for fornecedor in fornecedores:
                st.write(f"Nome do Fornecedor: {fornecedor['nome_fornecedor']}, Cidade: {fornecedor['cidade']}, Estado: {fornecedor['estado']}, Produtos Fornecidos: {fornecedor['numero_de_produtos']}")
        else:
            st.write("Nenhum fornecedor encontrado com os critérios de filtro especificados.")


def mostrar_produtos_com_filtro():
    st.subheader("Filtrar Produtos")

    # Inputs para filtros dinâmicos
    tipo_de_peca = st.text_input("Tipo de Peça")
    preco_min = st.number_input("Preço mínimo", min_value=0.0, value=0.0)
    preco_max = st.number_input("Preço máximo", min_value=0.0, value=1000.0)
    estoque_min = st.number_input("Estoque mínimo", min_value=0, value=0)
    
    # Filtro para a quantidade em estoque
    q_em_estoque_max = st.number_input("Estoque máximo", min_value=0, value=1000)
    
    if st.button("Filtrar Produtos"):
        filtros = {}

        if tipo_de_peca:
            filtros["tipo_de_peca"] = tipo_de_peca
        if preco_min is not None and preco_max is not None:
            filtros["preco_de_venda"] = (preco_min, preco_max)
        if estoque_min is not None and q_em_estoque_max is not None:
            filtros["q_em_estoque"] = (estoque_min, q_em_estoque_max)

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        # Construção da consulta dinâmica com base nos filtros
        where_clauses = []
        params = []

        if "tipo_de_peca" in filtros:
            where_clauses.append("tipo_de_peca LIKE %s")
            params.append(f"%{filtros['tipo_de_peca']}%")
        
        if "preco_de_venda" in filtros:
            where_clauses.append("preco_de_venda BETWEEN %s AND %s")
            params.extend(filtros["preco_de_venda"])
        
        if "q_em_estoque" in filtros:
            where_clauses.append("q_em_estoque BETWEEN %s AND %s")
            params.extend(filtros["q_em_estoque"])

        where_query = " AND ".join(where_clauses)
        if where_query:
            where_query = "WHERE " + where_query

        query = f"SELECT * FROM Produto {where_query}"

        cursor.execute(query, tuple(params))
        produtos = cursor.fetchall()
        db.close()

        st.write("### Produtos Filtrados")
        if produtos:
            for produto in produtos:
                st.write(f"Tipo de Peça: {produto['tipo_de_peca']}, Preço: {produto['preco_de_venda']}, Estoque: {produto['q_em_estoque']}")
        else:
            st.write("Nenhum produto encontrado com os critérios de filtro especificados.")

def mostrar_sedes_com_filtro():
    st.subheader("Filtrar Sedes")

    # Inputs para filtros dinâmicos para sedes
    nome_sede = st.text_input("Nome da Sede")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    
    # Filtro para a quantidade de funcionários
    funcionarios_min = st.number_input("Número mínimo de Funcionários", min_value=0, value=0)
    funcionarios_max = st.number_input("Número máximo de Funcionários", min_value=0, value=1000)
    
    if st.button("Filtrar Sedes"):
        filtros = {}

        if nome_sede:
            filtros["nome_sede"] = nome_sede
        if cidade:
            filtros["cidade"] = cidade
        if estado:
            filtros["estado"] = estado
        if funcionarios_min is not None and funcionarios_max is not None:
            filtros["numero_de_funcionarios"] = (funcionarios_min, funcionarios_max)

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        # Construção da consulta dinâmica com base nos filtros
        where_clauses = []
        params = []

        if "nome_sede" in filtros:
            where_clauses.append("nome_sede LIKE %s")
            params.append(f"%{filtros['nome_sede']}%")
        
        if "cidade" in filtros:
            where_clauses.append("cidade LIKE %s")
            params.append(f"%{filtros['cidade']}%")
        
        if "estado" in filtros:
            where_clauses.append("estado LIKE %s")
            params.append(f"%{filtros['estado']}%")
        
        if "numero_de_funcionarios" in filtros:
            where_clauses.append("numero_de_funcionarios BETWEEN %s AND %s")
            params.extend(filtros["numero_de_funcionarios"])

        where_query = " AND ".join(where_clauses)
        if where_query:
            where_query = "WHERE " + where_query

        query = f"SELECT * FROM Sede {where_query}"

        cursor.execute(query, tuple(params))
        sedes = cursor.fetchall()
        db.close()

        st.write("### Sedes Filtradas")
        if sedes:
            for sede in sedes:
                st.write(f"Nome da Sede: {sede['nome_sede']}, Cidade: {sede['cidade']}, Estado: {sede['estado']}, Funcionários: {sede['numero_de_funcionarios']}")
        else:
            st.write("Nenhuma sede encontrada com os critérios de filtro especificados.")


def mostrar_clientes_com_filtro():
    st.subheader("Filtrar Clientes")

    # Inputs para filtros dinâmicos para clientes
    nome_cliente = st.text_input("Nome do Cliente")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    
    # Filtro para a quantidade de compras ou outro critério
    compras_min = st.number_input("Número mínimo de Compras", min_value=0, value=0)
    compras_max = st.number_input("Número máximo de Compras", min_value=0, value=1000)
    
    if st.button("Filtrar Clientes"):
        filtros = {}

        if nome_cliente:
            filtros["nome_cliente"] = nome_cliente
        if cidade:
            filtros["cidade"] = cidade
        if estado:
            filtros["estado"] = estado
        if compras_min is not None and compras_max is not None:
            filtros["numero_de_compras"] = (compras_min, compras_max)

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        # Construção da consulta dinâmica com base nos filtros
        where_clauses = []
        params = []

        if "nome_cliente" in filtros:
            where_clauses.append("nome_cliente LIKE %s")
            params.append(f"%{filtros['nome_cliente']}%")
        
        if "cidade" in filtros:
            where_clauses.append("cidade LIKE %s")
            params.append(f"%{filtros['cidade']}%")
        
        if "estado" in filtros:
            where_clauses.append("estado LIKE %s")
            params.append(f"%{filtros['estado']}%")
        
        if "numero_de_compras" in filtros:
            where_clauses.append("numero_de_compras BETWEEN %s AND %s")
            params.extend(filtros["numero_de_compras"])

        where_query = " AND ".join(where_clauses)
        if where_query:
            where_query = "WHERE " + where_query

        query = f"SELECT * FROM Cliente {where_query}"

        cursor.execute(query, tuple(params))
        clientes = cursor.fetchall()
        db.close()

        st.write("### Clientes Filtrados")
        if clientes:
            for cliente in clientes:
                st.write(f"Nome do Cliente: {cliente['nome_cliente']}, Cidade: {cliente['cidade']}, Estado: {cliente['estado']}, Compras: {cliente['numero_de_compras']}")
        else:
            st.write("Nenhum cliente encontrado com os critérios de filtro especificados.")

def mostrar_pedidos_com_filtro():
    st.subheader("Filtrar Pedidos")

    # Inputs para filtros dinâmicos para pedidos
    numero_pedido = st.text_input("Número do Pedido")
    data_inicio = st.date_input("Data de Início do Pedido")
    data_fim = st.date_input("Data de Fim do Pedido")
    status_pedido = st.selectbox("Status do Pedido", ["", "Pendente", "Enviado", "Entregue", "Cancelado"])
    
    # Filtro para o valor total do pedido
    valor_min = st.number_input("Valor mínimo do Pedido", min_value=0.0, value=0.0)
    valor_max = st.number_input("Valor máximo do Pedido", min_value=0.0, value=10000.0)
    
    # Filtro para o cliente
    nome_cliente = st.text_input("Nome do Cliente")

    if st.button("Filtrar Pedidos"):
        filtros = {}

        if numero_pedido:
            filtros["numero_pedido"] = numero_pedido
        if data_inicio:
            filtros["data_pedido_inicio"] = data_inicio
        if data_fim:
            filtros["data_pedido_fim"] = data_fim
        if status_pedido:
            filtros["status_pedido"] = status_pedido
        if valor_min is not None and valor_max is not None:
            filtros["valor_total"] = (valor_min, valor_max)
        if nome_cliente:
            filtros["nome_cliente"] = nome_cliente

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        # Construção da consulta dinâmica com base nos filtros
        where_clauses = []
        params = []

        if "numero_pedido" in filtros:
            where_clauses.append("numero_pedido LIKE %s")
            params.append(f"%{filtros['numero_pedido']}%")
        
        if "data_pedido_inicio" in filtros and "data_pedido_fim" in filtros:
            where_clauses.append("data_pedido BETWEEN %s AND %s")
            params.extend([filtros["data_pedido_inicio"], filtros["data_pedido_fim"]])
        
        if "status_pedido" in filtros:
            where_clauses.append("status_pedido = %s")
            params.append(filtros["status_pedido"])
        
        if "valor_total" in filtros:
            where_clauses.append("valor_total BETWEEN %s AND %s")
            params.extend(filtros["valor_total"])

        if "nome_cliente" in filtros:
            where_clauses.append("nome_cliente LIKE %s")
            params.append(f"%{filtros['nome_cliente']}%")

        where_query = " AND ".join(where_clauses)
        if where_query:
            where_query = "WHERE " + where_query

        query = f"SELECT * FROM Pedido {where_query}"

        cursor.execute(query, tuple(params))
        pedidos = cursor.fetchall()
        db.close()

        st.write("### Pedidos Filtrados")
        if pedidos:
            for pedido in pedidos:
                st.write(f"Número do Pedido: {pedido['numero_pedido']}, Data: {pedido['data_pedido']}, Status: {pedido['status_pedido']}, Valor: {pedido['valor_total']}, Cliente: {pedido['nome_cliente']}")
        else:
            st.write("Nenhum pedido encontrado com os critérios de filtro especificados.")

def mostrar_funcionarios_com_filtro():
    st.subheader("Filtrar Funcionários")
    
    nome_funcionario = st.text_input("Nome do Funcionário")
    cargo = st.text_input("Cargo")
    data_inicio = st.date_input("Data de Início da Contratação", None)
    data_fim = st.date_input("Data de Fim da Contratação", None)
    salario_min = st.number_input("Salário mínimo", min_value=0.0, value=0.0)
    salario_max = st.number_input("Salário máximo", min_value=0.0, value=10000.0)
    nome_sede = st.text_input("Nome da Sede")

    if st.button("Filtrar Funcionários"):
        filtros = {}
        
        # Adiciona filtros somente se os campos não estão vazios ou nulos
        if nome_funcionario:
            filtros["nome_funcionario"] = nome_funcionario
        if cargo:
            filtros["cargo"] = cargo
        if data_inicio and data_fim:
            filtros["data_contratacao"] = (data_inicio, data_fim)
        if salario_min is not None and salario_max is not None:
            filtros["salario"] = (salario_min, salario_max)
        if nome_sede:
            filtros["nome_sede"] = nome_sede

        colunas = ["nome_funcionario", "cargo", "data_contratacao", "salario", "nome_sede"]
        funcionarios = aplicar_filtros("Funcionario", filtros, colunas)

        st.write("### Funcionários Filtrados")
        if funcionarios:
            for func in funcionarios:
                st.write(f"Nome: {func['nome_funcionario']}, Cargo: {func['cargo']}, Salário: {func['salario']}, Sede: {func['nome_sede']}")
        else:
            st.write("Nenhum funcionário encontrado.")

# Layout do Streamlit
def main():
    st.title("Gestão de Loja de Roupas")

    menu = [
        "Fornecedores", "Adicionar Fornecedor", "Clientes", "Adicionar Cliente", 
        "Produtos", "Adicionar Produto", "Sedes", "Adicionar Sede", 
        "Funcionários", "Adicionar Funcionário", "Pedidos", "Adicionar Pedido",
        "Filtrar Produtos", "Filtrar Sedes", "Filtrar Clientes", "Filtrar Fornecedores", "Filtrar Pedidos", "Filtrar Funcionários"
    ]
    escolha = st.sidebar.selectbox("Escolha uma opção", menu)

    if escolha == "Fornecedores":
        mostrar_fornecedores()
    elif escolha == "Adicionar Fornecedor":
        adicionar_fornecedor()
    elif escolha == "Clientes":
        mostrar_clientes()
    elif escolha == "Adicionar Cliente":
        adicionar_cliente()
    elif escolha == "Produtos":
        mostrar_produtos()
    elif escolha == "Adicionar Produto":
        adicionar_produto()
    elif escolha == "Sedes":
        mostrar_sedes()
    elif escolha == "Adicionar Sede":
        adicionar_sede()
    elif escolha == "Funcionários":
        mostrar_funcionarios()
    elif escolha == "Adicionar Funcionário":
        adicionar_funcionario()
    elif escolha == "Pedidos":
        mostrar_pedidos()
    elif escolha == "Adicionar Pedido":
        adicionar_pedido()
    elif escolha == "Filtrar Produtos":
        mostrar_produtos_com_filtro()
    elif escolha == "Filtrar Sedes":
        mostrar_sedes_com_filtro()
    elif escolha == "Filtrar Clientes":
        mostrar_clientes_com_filtro()
    elif escolha == "Filtrar Fornecedores":
        mostrar_fornecedores_com_filtro()
    elif escolha == "Filtrar Pedidos":
        mostrar_pedidos_com_filtro()
    elif escolha == "Filtrar Funcionários":
        mostrar_funcionarios_com_filtro()
    




if __name__ == "__main__":
    main()
