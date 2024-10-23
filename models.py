from app import db
import bcrypt

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def set_password(self, senha):
        """Criptografa a senha e a armazena."""
        self.senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, senha):
        """Verifica se a senha fornecida corresponde à senha armazenada."""
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    curso = db.Column(db.String(100), default="Generation Brasil - 1")
