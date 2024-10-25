from flask import request, jsonify
from app import app, db
from models import Funcionario, Aluno
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Rotas para Funcionario
@app.route('/funcionario', methods=['POST'])
def create_funcionario():
    """Cria um novo funcionário."""
    data = request.get_json()
    if Funcionario.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400
    hashed_password = generate_password_hash(data['senha'], method='pbkdf2:sha256')
    new_funcionario = Funcionario(nome=data['nome'], email=data['email'], senha=hashed_password)
    db.session.add(new_funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário criado com sucesso"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Faz login de um funcionário e retorna um token JWT."""
    data = request.get_json()
    funcionario = Funcionario.query.filter_by(email=data['email']).first()
    if funcionario and check_password_hash(funcionario.senha, data['senha']):
        access_token = create_access_token(identity=funcionario.id, expires_delta=False)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/funcionario/<int:id>', methods=['GET'])
@jwt_required()
def get_funcionario(id):
    """Obtém os detalhes de um funcionário pelo ID."""
    funcionario = Funcionario.query.get_or_404(id)
    return jsonify({
        'id': funcionario.id,
        'nome': funcionario.nome,
        'email': funcionario.email
    })

@app.route('/funcionario/<int:id>', methods=['PUT'])
@jwt_required()
def update_funcionario(id):
    """Atualiza os detalhes de um funcionário pelo ID."""
    data = request.get_json()
    funcionario = Funcionario.query.get_or_404(id)
    funcionario.nome = data['nome']
    funcionario.email = data['email']
    if 'senha' in data:
        funcionario.senha = generate_password_hash(data['senha'], method='pbkdf2:sha256')
    db.session.commit()
    return jsonify({"message": "Funcionário atualizado com sucesso"}), 200

@app.route('/funcionario/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_funcionario(id):
    """Remove um funcionário pelo ID."""
    funcionario = Funcionario.query.get_or_404(id)
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário removido com sucesso"}), 200

# Rotas para Aluno
@app.route('/aluno', methods=['POST'])
@jwt_required()
def create_aluno():
    """Cria um novo aluno."""
    data = request.get_json()

    # Valida se o e-mail já está cadastrado
    if Aluno.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400

    # Valida o comprimento do nome
    if len(data['nome']) < 3:
        return jsonify({"error": "Nome deve ter pelo menos 3 caracteres"}), 400

    # Valida a idade
    if data.get('idade', None) is not None and data['idade'] < 0:
        return jsonify({"error": "Idade deve ser um valor positivo"}), 400

    # Criação do novo aluno
    new_aluno = Aluno(
        nome=data['nome'],
        email=data['email'],
        idade=data.get('idade'),
        notaprimeiromodulo=data.get('nota_primeiro_modulo'),
        notasegundomodulo=data.get('nota_segundo_modulo')
    )

    # Adiciona o novo aluno ao banco de dados
    db.session.add(new_aluno)
    db.session.commit()

    return jsonify({"message": "Aluno criado com sucesso", "id": new_aluno.id}), 201

@app.route('/aluno/<int:id>', methods=['GET'])
@jwt_required()
def get_aluno(id):
    """Obtém os detalhes de um aluno pelo ID."""
    aluno = Aluno.query.get_or_404(id)
    return jsonify({
        'id': aluno.id,
        'nome': aluno.nome,
        'email': aluno.email
    })

@app.route('/aluno/<int:id>', methods=['PUT'])
@jwt_required()
def update_aluno(id):
    """Atualiza os detalhes de um aluno pelo ID."""
    data = request.get_json()
    aluno = Aluno.query.get_or_404(id)
    aluno.nome = data['nome']
    aluno.email = data['email']
    db.session.commit()
    return jsonify({"message": "Aluno atualizado com sucesso"}), 200

@app.route('/aluno/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_aluno(id):
    """Remove um aluno pelo ID."""
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno removido com sucesso"}), 200

# Você pode adicionar mais rotas aqui conforme necessário.
