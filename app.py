import os
import time
from datetime import datetime
from flask import Flask, jsonify, request, render_template
import mysql.connector 

app = Flask(__name__)

#conectar_banco()
#listar_profissionais()
#buscar_horarios_ocupados
#criar_agendamento()

def conectar_banco():
    for tentativa in range(5):
        try:
            conexao = mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'localhost'),
                port=int(os.environ.get('DB_PORT', 3307)),
                user=os.environ.get('DB_USER', 'root'),
                password=os.environ.get('DB_PASSWORD', 'agend##77'),
                database=os.environ.get('DB_NAME', 'salao_db')
            )
            return conexao 
        except mysql.connector.Error as erro:
            print(f'Falha na conexão (Tentativa {tentativa+1}/5): {erro}')
            time.sleep(2)
    return None

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/profissionais', methods=['GET'])
def listar_profissionais():
    db = conectar_banco()
    if not db:
        return jsonify({"erro": "Erro interno do servidor: Falha de conexão com o banco"}), 500
    cursor = db.cursor(dictionary = True)
    try:
        cursor.execute('SELECT prof_id, prof_nome, prof_especialidade FROM profissionais;')
        profissionais = cursor.fetchall()
        return jsonify(profissionais), 200
    except mysql.connector.Error as erro_sql:
        return jsonify({'erro': str(erro_sql)}), 500
    finally: 
        cursor.close()
        db.close()

@app.route('/horarios-ocupados', methods=['GET'])
def buscar_horarios_ocupados():
    prof_id = request.args.get('profissional_id')
    data_escolhida = request.args.get('data')

    if not prof_id or not data_escolhida:
        return jsonify([]), 200

    db = conectar_banco()
    if not db:
        return jsonify({'erro': 'Erro de conexão com o banco'}), 500

    cursor = db.cursor(dictionary=True)
    try:
        query = """
            SELECT TIME(data_hora) as hora_ocupada
            FROM agendamentos
            WHERE prof_id = %s AND DATE(data_hora) = %s;
        """
        cursor.execute(query, (prof_id, data_escolhida))
        resultados = cursor.fetchall()

        lista_ocupados = [str(linha['hora_ocupada']) for linha in resultados]
        return jsonify(lista_ocupados), 200
    except mysql.connector.Error as erro_sql:
        return jsonify({"erro": str(erro_sql)}), 500
    finally:
        cursor.close()
        db.close()

@app.route('/agendar', methods=['POST'])
def criar_agendamento():
    dados = request.get_json()
    if not dados:
       return jsonify({"erro": "Corpo da requisição vazio"}), 400
    
    prof_id = dados.get('profissional_id')
    cli_id = dados.get('cliente_id')
    data_hora_string = dados.get('data_hora')

    if not all([prof_id, cli_id, data_hora_string]):
        return jsonify({"erro": "Parâmetros obrigatórios ausentes"}), 400
#verificar
    try:
        data_hora_obj = datetime.strptime(data_hora_string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({"erro": "Formato de data inválido. O correto é YYYY-MM-DD HH:MM:SS"}), 400

    db = conectar_banco()
    if not db:
        return jsonify({"erro": "Erro de conexão com o banco"}), 500

    cursor = db.cursor(dictionary=True)

    try:
        # 1. Validação de Conflito
        query_verificacao = "SELECT agend_id FROM agendamentos WHERE prof_id = %s AND data_hora = %s;"
        cursor.execute(query_verificacao, (prof_id, data_hora_obj))
        
        if cursor.fetchone():
            return jsonify({"erro": "Horário indisponível. Já existe um agendamento."}), 409

        # 2. Inserção do Registro
        query_insercao = "INSERT INTO agendamentos (prof_id, cli_id, data_hora) VALUES (%s, %s, %s);"
        cursor.execute(query_insercao, (prof_id, cli_id, data_hora_obj))
        db.commit()

        return jsonify({"mensagem": "Agendamento gravado com sucesso!"}), 201
    
    except mysql.connector.Error as erro_sql:
        db.rollback() # Desfaz qualquer alteração pendente em caso de falha
        return jsonify({"erro": str(erro_sql)}), 500
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)