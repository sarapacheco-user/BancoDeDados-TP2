from connection import get_db_connection

try:
    db = get_db_connection()
    
    db.ping(reconnect=True) 
    print("Conexão bem-sucedida!")
    db.close()
except Exception as e:
    print(f"Erro: {e}")
