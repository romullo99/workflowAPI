from flask import Flask, request, jsonify

app = Flask(__name__)
mensagens = []

@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(mensagens), 200

@app.route('/mensagens', methods=['POST'])
def adicionar_mensagem():
    dadas = request.get_json()

    if not dadas or 'texto' not in dadas:
        return jsonify({'erro': 'Campo "texto" é obrigatório'}), 400

    nova_mensagem = {
        'id': len(mensagens) + 1,
        'texto': dadas['texto']
    }

    mensagens.append(nova_mensagem)
    return jsonify(nova_mensagem), 201

if __name__ == '__main__':
    app.run(debug=True)
