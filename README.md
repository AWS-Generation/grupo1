## API de Funcionários e Alunos

My Flask App é uma aplicação web desenvolvida com Flask, que oferece uma API para gerenciar funcionários e autenticação de login. Esta aplicação é ideal para aprender e praticar conceitos de desenvolvimento web, APIs RESTful e integração com Docker.

## Funcionalidades

- **Criação de Funcionários**: Adicione novos funcionários com nome, email e senha.
- **Autenticação de Login**: Realize login com email e senha.
- **Documentação Swagger**: Acesse a documentação interativa da API em `/swagger`.

## 💻 Pré-requisitos

- **Python 3.8+** 
- **Flask 2.0.1**
- **Docker 20.10.7**
- **PostgreSQL** (ou outro banco de dados configurado)

## 🚀 Instalação

### Clonando o Repositório

Clone este repositório utilizando o comando: git clone https://github.com/AWS-Generation/showcasegrupo1.git

## Windows, MacOS e Linux: 
Abra o Prompt de Comando ou o PowerShell.

Navegue até a pasta do projeto com o seguinte comando:
cd showcasegrupo1\My-flask-app

### Configurando o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt

### Configurando o Banco de Dados
Certifique-se de que o PostgreSQL está instalado e rodando.

### Executando a aplicação utilizando o Docker
Construindo a Imagem Docker
docker build -t my_flask_app .

### Rodando o Contêiner
docker run -d -p 5000:5000 my_flask_app

### Aplicação funcionando
Se tudo ocorrer bem, a aplicação estará disponível na web em http://localhost:5000

### Documentação da API
A documentação da API está disponível em http://localhost:5000/swagger.

## 🤝 Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="[https://media.licdn.com/dms/image/v2/C4D03AQHQVKpkGkubmQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1662130803394?e=1735171200&v=beta&t=z-8VkfgwWlgNXRREQHwt4iSMcGTVG4q71iZ2LX-6x7g)](https://media.licdn.com/dms/image/v2/C4D03AQHQVKpkGkubmQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1662130803394?e=1735171200&v=beta&t=z-8VkfgwWlgNXRREQHwt4iSMcGTVG4q71iZ2LX-6x7g)" width="100px;" alt="Vinicius Ferreira"/><br>
        <sub>
          <b>Vinicius Ferreira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://s2.glbimg.com/FUcw2usZfSTL6yCCGj3L3v3SpJ8=/smart/e.glbimg.com/og/ed/f/original/2019/04/25/zuckerberg_podcast.jpg" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Vinicius Nery</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Daniel Cordeiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

Este projeto foi feito durante o bootcamp da Generation Brasil (AWS).
