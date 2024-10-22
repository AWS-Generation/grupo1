## Descrição do projeto

My Flask App é uma aplicação web desenvolvida com Flask, que oferece uma API para gerenciar funcionários e autenticação de login. Esta aplicação é ideal para aprender e praticar conceitos de desenvolvimento web, APIs RESTful e integração com Docker.

## Funcionalidades

- **Criação de Funcionários**: Adicione novos funcionários com nome, email e senha.
- **Autenticação de Login**: Realize login com email e senha.
- **Documentação Swagger**: Acesse a documentação interativa da API em `/swagger`.

## Requisitos

- **Python 3.8+**
- **Flask 2.0.1**
- **Docker 20.10.7**
- **PostgreSQL** (ou outro banco de dados configurado)

## Instalação

### Clonando o Repositório

git clone https://github.com/AWS-Generation/showcasegrupo1.git
Vá para a pasta My-flask-app
cd showcasegrupo1/My-flask-app

### Configurando o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt

### Configurando o Banco de Dados
Certifique-se de que o PostgreSQL está instalado e rodando. Configure as variáveis de ambiente para a conexão com o banco de dados.

### Executando a aplicação
flask run
A aplicação estará disponível em http://localhost:5000

### Usando o Docker 
Construindo a Imagem Docker
docker build -t my_flask_app .

### Rodando o Contêiner
docker run -d -p 5000:5000 my_flask_app

### Documentação da API
A documentação da API está disponível em http://localhost:5000/swagger.

Este projeto foi feito durante o bootcamp da Generation Brasil (AWS).
