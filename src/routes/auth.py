from flask import Blueprint, jsonify, request, session
from src.models.visitor import Admin, db
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """Autentica um administrador"""
    try:
        data = request.json
        
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email e senha são obrigatórios'}), 400
        
        # Buscar administrador
        admin = Admin.query.filter_by(email=data['email']).first()
        
        if not admin or not admin.check_password(data['password']):
            return jsonify({'error': 'Email ou senha incorretos'}), 401
        
        # Atualizar último login
        admin.last_login = datetime.utcnow()
        db.session.commit()
        
        # Criar sessão
        session['admin_id'] = admin.id
        session['admin_email'] = admin.email
        
        return jsonify({
            'message': 'Login realizado com sucesso',
            'admin': admin.to_dict()
        })
        
    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Faz logout do administrador"""
    session.clear()
    return jsonify({'message': 'Logout realizado com sucesso'})

@auth_bp.route('/me', methods=['GET'])
def get_current_admin():
    """Obtém informações do administrador logado"""
    try:
        if 'admin_id' not in session:
            return jsonify({'error': 'Não autenticado'}), 401
        
        admin = Admin.query.get(session['admin_id'])
        if not admin:
            session.clear()
            return jsonify({'error': 'Administrador não encontrado'}), 404
        
        return jsonify(admin.to_dict())
        
    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

def require_auth(f):
    """Decorator para rotas que requerem autenticação"""
    from functools import wraps
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            return jsonify({'error': 'Não autenticado'}), 401
        return f(*args, **kwargs)
    return decorated_function

