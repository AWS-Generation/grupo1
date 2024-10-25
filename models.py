from app import db
import bcrypt

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False, default="Generation Brasil - 1")

    def set_password(self, senha):
        """Criptografa a senha e a armazena."""
        self.senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, senha):
        """Verifica se a senha fornecida corresponde à senha armazenada."""
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))

class Aluno(db.Model):
    __tablename__ = 'aluno'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=True)
    notaprimeiromodulo = db.Column(db.Float, nullable=True)
    notasegundomodulo = db.Column(db.Float, nullable=True)# Armazenaremos manualmente, pois SQLAlchemy não tem suporte direto para GENERATED

