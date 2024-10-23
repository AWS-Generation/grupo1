## API de Funcionários e Alunos (Bootcamp Generation Brasil)

Uma aplicação web desenvolvida com Flask, que oferece uma API para gerenciar funcionários e autenticação de login. Esta aplicação é ideal para aprender e praticar conceitos de desenvolvimento web, APIs RESTful e integração com Docker.

## Funcionalidades

- **Criação de Funcionários**: Adicione novos funcionários com nome, email e senha.
- **Autenticação de Login**: Realize login com email e senha.

## 💻 Pré-requisitos

- **Python 3.8+** 
- **Flask 2.0.1**
- **Docker 20.10.7**
- **PostgreSQL** (ou outro banco de dados configurado)

## 🚀 Instalação

### Clonando o Repositório

Clone este repositório utilizando o comando: 
```
git clone https://github.com/AWS-Generation/grupo1.git
```

## Windows, MacOS e Linux: 
Abra o Prompt de Comando ou o PowerShell.

Navegue até a pasta do projeto com o seguinte comando:
```
cd My-flask-app
```

### Configurando o ambiente virtual
Para o projeto funcionar, você deve instalar todos os requirimentos da aplicação
```
pip install -r requirements.txt
```

### Banco de Dados
Certifique-se de que o PostgreSQL está instalado e rodando.

### Executando a aplicação utilizando o Docker
Construindo a Imagem Docker
```
docker build -t my_flask_app .
```

### Rodando o Container
```
docker run -d -p 5000:5000 my_flask_app
```
### Aplicação funcionando
Se tudo ocorrer bem, a aplicação estará disponível na web em http://localhost:5000

### Documentação da API
A documentação da API está disponível em http://localhost:5000/swagger.

## 🤝 Colaboradores
Agradecimento especial aos companheiros de equipe que participaram deste projeto:
<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://media.licdn.com/dms/image/v2/C4D03AQHQVKpkGkubmQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1662130803394?e=1735171200&v=beta&t=z-8VkfgwWlgNXRREQHwt4iSMcGTVG4q71iZ2LX-6x7g" width="100px;" alt="Vinicius Ferreira"/><br>
        <sub>
          <b>Vinicius Ferreira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://media.licdn.com/dms/image/v2/D4E35AQERkia6rDCLwg/profile-framedphoto-shrink_800_800/profile-framedphoto-shrink_800_800/0/1635514188812?e=1730314800&v=beta&t=0TUYXUuiCuhcMGp8mJUxH-I59GQgaxbx1OZz4ZBI3H0" width="100px;" alt="Vincius Nery"/><br>
        <sub>
          <b>Vinicius Nery</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://media.licdn.com/dms/image/v2/C4D03AQFDNtXA880UFw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1662841146704?e=1735171200&v=beta&t=zr5OK0mCkCRlNj17pXNBp1ok7kq9qL2wuRjJ9-fxiJo" width="100px;" alt="Daniel Cordeiro"/><br>
        <sub>
          <b>Daniel Cordeiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

Este projeto foi feito durante o bootcamp da Generation Brasil (AWS).
