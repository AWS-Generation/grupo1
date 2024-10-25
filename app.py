from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@db:5432/projetogeneration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativar modificações de rastreamento
app.config['JWT_SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.bXAz_VJ0iLKu-Noq9tKXxYjRMD3P2l81HVAR45MZjVw'  
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Configuração do Swagger
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "My Flask App"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger_json():
    return send_from_directory(os.getcwd(), 'swagger.json')

# Importe suas rotas
from routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
