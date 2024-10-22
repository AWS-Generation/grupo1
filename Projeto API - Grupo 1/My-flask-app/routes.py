from flask import request, jsonify
from app import app, db
from models import Funcionario, Aluno
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/funcionario', methods=['POST'])
def create_funcionario():
    data = request.get_json()
    if Funcionario.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400
    new_funcionario = Funcionario(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(new_funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário criado com sucesso"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    funcionario = Funcionario.query.filter_by(email=data['email'], senha=data['senha']).first()
    if not funcionario:
        return jsonify({"error": "Credenciais inválidas"}), 401
    access_token = create_access_token(identity=funcionario.id, expires_delta=False)
    return jsonify(access_token=access_token), 200

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

# Outras rotas CRUD (GET, PUT, DELETE) para Funcionario e Aluno
