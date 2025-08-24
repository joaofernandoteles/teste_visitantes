from src.models.user import db
from datetime import datetime
import uuid
import hashlib

class Visitor(db.Model):
    __tablename__ = 'visitors'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    consentimento = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_hash = db.Column(db.String(64), nullable=True)
    origem = db.Column(db.String(50), nullable=False, default='culto_domingo')
    status = db.Column(db.String(20), nullable=False, default='novo')
    nota = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Visitor {self.nome}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'idade': self.idade,
            'consentimento': self.consentimento,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'ip_hash': self.ip_hash,
            'origem': self.origem,
            'status': self.status,
            'nota': self.nota
        }

    @staticmethod
    def hash_ip(ip_address):
        """Hash do endereço IP para anonimização"""
        if not ip_address:
            return None
        return hashlib.sha256(ip_address.encode()).hexdigest()


class Admin(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Admin {self.email}>'

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_login': self.last_login.isoformat() if self.last_login else None
        }

    @staticmethod
    def hash_password(password):
        """Hash da senha usando SHA256 (em produção, usar bcrypt)"""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Verifica se a senha está correta"""
        return self.senha_hash == self.hash_password(password)

