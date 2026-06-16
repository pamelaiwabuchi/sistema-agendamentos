import os
from flask import Flask, jsonify, request, render_template
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def conectar_banco():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'agend##77'),
        database=os.environ.get('DB_NAME', 'salao_db')
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profissionais', methods=['GET'])
def listar():
    db = conectar_banco()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM profissionais")
    res = cursor.fetchall()
    cursor.close(); db.close()
    return jsonify(res)

@app.route('/horarios-ocupados', methods=['GET'])
def buscar_ocupados():
    prof_id = request.args.get('profissional_id')
    data = request.args.get('data')
    db = conectar_banco()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT TIME(data_hora) as hora FROM agendamentos WHERE prof_id = %s AND DATE(data_hora) = %s", (prof_id, data))
    res = [str(r['hora']) for r in cursor.fetchall()]
    cursor.close(); db.close()
    return jsonify(res)

@app.route('/agendar', methods=['POST'])
def agendar():
    dados = request.get_json()
    db = conectar_banco()
    cursor = db.cursor()
    try:
        # Colunas corrigidas para cli_nome e cli_email
        query = "INSERT INTO agendamentos (cli_nome, cli_email, prof_id, data_hora) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (dados['nome'], dados['email'], dados['profissional_id'], dados['data_hora']))
        db.commit()
        return jsonify({"mensagem": "Agendamento confirmado!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        cursor.close(); db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)