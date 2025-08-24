from flask import Blueprint, jsonify, request
from src.models.visitor import Visitor, db
from datetime import datetime
import re

visitor_bp = Blueprint('visitor', __name__)

def validate_phone(phone):
    """Valida se o telefone está no formato brasileiro"""
    # Remove caracteres não numéricos
    numbers_only = re.sub(r'\D', '', phone)
    return len(numbers_only) == 11

def validate_visitor_data(data):
    """Valida os dados do visitante"""
    errors = {}
    
    if not data.get('nome', '').strip():
        errors['nome'] = 'Nome é obrigatório'
    
    if not data.get('telefone', '').strip():
        errors['telefone'] = 'Telefone é obrigatório'
    elif not validate_phone(data['telefone']):
        errors['telefone'] = 'Telefone deve ter 11 dígitos'
    
    if not data.get('idade'):
        errors['idade'] = 'Idade é obrigatória'
    else:
        try:
            idade = int(data['idade'])
            if idade < 12 or idade > 120:
                errors['idade'] = 'Idade deve ser entre 12 e 120 anos'
        except (ValueError, TypeError):
            errors['idade'] = 'Idade deve ser um número válido'
    
    if not data.get('consentimento'):
        errors['consentimento'] = 'É necessário autorizar o uso dos dados'
    
    return errors

@visitor_bp.route('/visitors', methods=['POST'])
def create_visitor():
    """Cria um novo visitante"""
    try:
        data = request.json
        
        # Validar dados
        errors = validate_visitor_data(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Obter IP do cliente
        client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
        
        # Criar visitante
        visitor = Visitor(
            nome=data['nome'].strip(),
            telefone=data['telefone'].strip(),
            idade=int(data['idade']),
            consentimento=bool(data['consentimento']),
            ip_hash=Visitor.hash_ip(client_ip),
            origem=data.get('origem', 'culto_domingo'),
            status='novo'
        )
        
        db.session.add(visitor)
        db.session.commit()
        
        return jsonify({
            'message': 'Visitante registrado com sucesso!',
            'visitor': visitor.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@visitor_bp.route('/visitors', methods=['GET'])
def get_visitors():
    """Lista todos os visitantes com filtros opcionais"""
    try:
        # Parâmetros de filtro
        search = request.args.get('search', '').strip()
        status_filter = request.args.get('status', '').strip()
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 50))
        
        # Query base
        query = Visitor.query
        
        # Aplicar filtros
        if search:
            query = query.filter(
                db.or_(
                    Visitor.nome.ilike(f'%{search}%'),
                    Visitor.telefone.ilike(f'%{search}%')
                )
            )
        
        if status_filter:
            query = query.filter(Visitor.status == status_filter)
        
        # Ordenar por data de criação (mais recentes primeiro)
        query = query.order_by(Visitor.created_at.desc())
        
        # Paginação
        visitors = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        return jsonify({
            'visitors': [visitor.to_dict() for visitor in visitors.items],
            'total': visitors.total,
            'pages': visitors.pages,
            'current_page': page,
            'per_page': per_page
        })
        
    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

@visitor_bp.route('/visitors/<visitor_id>', methods=['GET'])
def get_visitor(visitor_id):
    """Obtém um visitante específico"""
    try:
        visitor = Visitor.query.get_or_404(visitor_id)
        return jsonify(visitor.to_dict())
    except Exception as e:
        return jsonify({'error': 'Visitante não encontrado'}), 404

@visitor_bp.route('/visitors/<visitor_id>', methods=['PUT'])
def update_visitor(visitor_id):
    """Atualiza um visitante"""
    try:
        visitor = Visitor.query.get_or_404(visitor_id)
        data = request.json
        
        # Campos que podem ser atualizados
        if 'telefone' in data:
            if validate_phone(data['telefone']):
                visitor.telefone = data['telefone'].strip()
            else:
                return jsonify({'error': 'Telefone inválido'}), 400
        
        if 'idade' in data:
            try:
                idade = int(data['idade'])
                if 12 <= idade <= 120:
                    visitor.idade = idade
                else:
                    return jsonify({'error': 'Idade deve ser entre 12 e 120 anos'}), 400
            except (ValueError, TypeError):
                return jsonify({'error': 'Idade deve ser um número válido'}), 400
        
        if 'status' in data:
            visitor.status = data['status']
        
        if 'nota' in data:
            visitor.nota = data['nota']
        
        db.session.commit()
        return jsonify(visitor.to_dict())
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@visitor_bp.route('/visitors/<visitor_id>', methods=['DELETE'])
def delete_visitor(visitor_id):
    """Exclui um visitante"""
    try:
        visitor = Visitor.query.get_or_404(visitor_id)
        db.session.delete(visitor)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@visitor_bp.route('/visitors/stats', methods=['GET'])
def get_visitor_stats():
    """Obtém estatísticas dos visitantes"""
    try:
        from datetime import datetime, timedelta
        
        # Total de visitantes
        total = Visitor.query.count()
        
        # Visitantes desta semana
        week_ago = datetime.utcnow() - timedelta(days=7)
        this_week = Visitor.query.filter(Visitor.created_at >= week_ago).count()
        
        # Novos contatos (status = 'novo')
        new_contacts = Visitor.query.filter(Visitor.status == 'novo').count()
        
        return jsonify({
            'total': total,
            'this_week': this_week,
            'new_contacts': new_contacts
        })
        
    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

