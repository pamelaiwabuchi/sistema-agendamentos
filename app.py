from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

def conectar_banco():
    for i in range(5):
        try:
            return mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'db'),
                user=os.environ.get('DB_USER', 'pamela'),
                password=os.environ.get('DB_PASSWORD', '12345678'),
                database=os.environ.get('DB_NAME', 'dbfatec')
            )
        except mysql.connector.Error:
            time.sleep(2)
    return None

@app.route('/')
def home():
    db = conectar_banco()
    if db and db.is_connected():
        status_banco = "Conexão com o MySQL funcionou com sucesso!"
        db.close()
    else:
        status_banco = "Não foi possível conectar ao banco de dados."

    return f"""
    <html>
        <head><title>Teste Aula Jean</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>Olá! Meu site Flask está rodando dentro do Docker!</h1>
            <p><strong>Status do Banco:</strong> {status_banco}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
