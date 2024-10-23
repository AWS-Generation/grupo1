from flask import request, jsonify
from app import app, db
from models import Funcionario, Aluno
from flask_jwt_extended import create_access_token, jwt_required

# Rota para criar um novo Funcionário
@app.route('/funcionario', methods=['POST'])
def create_funcionario():
    data = request.get_json()
    if Funcionario.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400
    new_funcionario = Funcionario(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(new_funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário criado com sucesso"}), 201

# Rota para fazer login de um Funcionário
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    funcionario = Funcionario.query.filter_by(email=data['email'], senha=data['senha']).first()
    if not funcionario:
        return jsonify({"error": "Credenciais inválidas"}), 401
    access_token = create_access_token(identity=funcionario.id, expires_delta=False)
    return jsonify(access_token=access_token), 200

# Rota para criar um novo Aluno (protegida)
@app.route('/aluno', methods=['POST'])
@jwt_required()
def create_aluno():
    data = request.get_json()
    if Aluno.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400
    new_aluno = Aluno(nome=data['nome'], email=data['email'])
    db.session.add(new_aluno)
    db.session.commit()
    return jsonify({"message": "Aluno criado com sucesso"}), 201

# Rota para obter todos os Funcionários
@app.route('/funcionario', methods=['GET'])
def get_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([{"id": f.id, "nome": f.nome, "email": f.email} for f in funcionarios]), 200

# Rota para obter um Funcionário por ID
@app.route('/funcionario/<int:id>', methods=['GET'])
def get_funcionario(id):
    funcionario = Funcionario.query.get(id)
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404
    return jsonify({"id": funcionario.id, "nome": funcionario.nome, "email": funcionario.email}), 200

# Rota para atualizar um Funcionário por ID
@app.route('/funcionario/<int:id>', methods=['PUT'])
@jwt_required()
def update_funcionario(id):
    data = request.get_json()
    funcionario = Funcionario.query.get(id)
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404
    funcionario.nome = data['nome']
    funcionario.email = data['email']
    db.session.commit()
    return jsonify({"message": "Funcionário atualizado com sucesso"}), 200

# Rota para deletar um Funcionário por ID
@app.route('/funcionario/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_funcionario(id):
    funcionario = Funcionario.query.get(id)
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário deletado com sucesso"}), 200

# Rota para obter todos os Alunos
@app.route('/aluno', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([{"id": a.id, "nome": a.nome, "email": a.email} for a in alunos]), 200

# Rota para obter um Aluno por ID
@app.route('/aluno/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404
    return jsonify({"id": aluno.id, "nome": aluno.nome, "email": aluno.email}), 200

# Rota para atualizar um Aluno por ID
@app.route('/aluno/<int:id>', methods=['PUT'])
@jwt_required()
def update_aluno(id):
    data = request.get_json()
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404
    aluno.nome = data['nome']
    aluno.email = data['email']
    db.session.commit()
    return jsonify({"message": "Aluno atualizado com sucesso"}), 200

# Rota para deletar um Aluno por ID
@app.route('/aluno/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno deletado com sucesso"}), 200
