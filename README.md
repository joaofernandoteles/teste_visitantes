# Sistema de Registro de Visitantes - Igreja

Um sistema web simples e profissional para registro de visitantes de cultos, desenvolvido com React (frontend) e Flask (backend), integrados em uma única aplicação.

## 📋 Índice

- [Características](#características)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [API Endpoints](#api-endpoints)
- [Deploy com Docker](#deploy-com-docker)
- [Contribuição](#contribuição)

## ✨ Características

### Funcionalidades Principais
- **Registro de Visitantes**: Formulário simples e intuitivo para captura de dados
- **Dashboard Administrativo**: Interface completa para gerenciamento de registros
- **Autenticação Segura**: Sistema de login para área administrativa
- **Busca e Filtros**: Localização rápida de visitantes por nome ou telefone
- **Exportação de Dados**: Download de relatórios em formato CSV
- **Design Responsivo**: Interface adaptável para desktop e mobile
- **Validações Completas**: Validação de dados no frontend e backend

### Características Técnicas
- **Sistema Integrado**: Frontend e backend servidos em uma única aplicação
- **Banco de Dados SQLite**: Configuração simples sem dependências externas
- **CORS Configurado**: Comunicação segura entre frontend e backend
- **Sessões Persistentes**: Autenticação mantida entre sessões
- **Containerização**: Deploy simplificado com Docker

## 🛠 Tecnologias Utilizadas

### Frontend
- **React 18**: Biblioteca JavaScript para interfaces de usuário
- **Vite**: Build tool moderna e rápida
- **Tailwind CSS**: Framework CSS utilitário
- **React Router**: Roteamento do lado do cliente
- **Lucide React**: Ícones modernos e consistentes

### Backend
- **Flask**: Framework web Python minimalista
- **SQLAlchemy**: ORM para Python
- **Flask-CORS**: Middleware para Cross-Origin Resource Sharing
- **SQLite**: Banco de dados leve e integrado
- **Werkzeug**: Utilitários WSGI para Flask

### DevOps
- **Docker**: Containerização da aplicação
- **Python 3.11**: Versão estável do Python
- **Node.js 20**: Runtime JavaScript para build do frontend




## 🏗 Arquitetura do Sistema

O sistema utiliza uma arquitetura integrada onde o Flask serve tanto as APIs REST quanto os arquivos estáticos do frontend React buildado.

```
┌─────────────────────────────────────────────────────────────┐
│                    Sistema Integrado                        │
├─────────────────────────────────────────────────────────────┤
│  Frontend (React)           │  Backend (Flask)              │
│  ├── Páginas                │  ├── APIs REST                │
│  │   ├── Home (/)           │  │   ├── /api/visitors        │
│  │   ├── Visitar (/visitar) │  │   ├── /api/auth            │
│  │   └── Admin (/admin)     │  │   └── /api/visitors/stats  │
│  ├── Componentes UI         │  ├── Modelos                  │
│  ├── Validações             │  │   ├── Visitor             │
│  └── Roteamento             │  │   └── User                │
│                              │  ├── Autenticação           │
│                              │  └── Banco SQLite           │
└─────────────────────────────────────────────────────────────┘
```

### Fluxo de Dados
1. **Registro de Visitante**: Frontend → API `/api/visitors` → Banco de Dados
2. **Login Admin**: Frontend → API `/api/auth/login` → Sessão Flask
3. **Dashboard**: Frontend → APIs `/api/visitors` e `/api/visitors/stats` → Dados em tempo real

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.11 ou superior
- Node.js 20 ou superior (apenas para desenvolvimento do frontend)
- Git

### Instalação Local

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd visitor-registration-backend
```

2. **Configure o ambiente Python**
```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

3. **Execute a aplicação**
```bash
python src/main.py
```

4. **Acesse o sistema**
- Aplicação: http://localhost:5000
- Área administrativa: http://localhost:5000/admin

### Credenciais Padrão
- **Email**: admin@igreja.com
- **Senha**: admin123

> ⚠️ **Importante**: Altere as credenciais padrão em produção editando o arquivo `src/main.py`

## 📱 Como Usar

### Para Visitantes

1. **Acesse a página inicial**: http://localhost:5000
2. **Clique em "Registrar Visita"** ou aguarde o redirecionamento automático
3. **Preencha o formulário** com:
   - Nome completo
   - WhatsApp/Telefone (com DDD)
   - Idade
   - Autorização para contato (obrigatório)
4. **Clique em "Fazer parte"** para enviar o registro
5. **Confirmação**: Página de sucesso será exibida

### Para Administradores

1. **Acesse a área administrativa**: http://localhost:5000/admin
2. **Faça login** com as credenciais administrativas
3. **Dashboard disponível**:
   - **Estatísticas**: Total de visitantes, visitantes da semana, novos contatos
   - **Lista de visitantes**: Visualização completa dos registros
   - **Busca**: Pesquise por nome ou telefone
   - **Exportação**: Download dos dados em formato CSV
   - **Ações**: Botões para contato, edição e exclusão (interface preparada)

### Funcionalidades do Dashboard

- **Visualização em tempo real**: Dados atualizados automaticamente
- **Busca inteligente**: Pesquisa por nome ou telefone
- **Exportação CSV**: Download completo dos registros
- **Status dos visitantes**: Classificação (novo, contatado, membro)
- **Informações detalhadas**: Data/hora do registro, dados de contato


## 📁 Estrutura do Projeto

```
visitor-registration-backend/
├── src/                          # Código fonte da aplicação
│   ├── main.py                   # Arquivo principal do Flask
│   ├── models/                   # Modelos de dados
│   │   ├── __init__.py
│   │   ├── user.py              # Modelo do usuário administrativo
│   │   └── visitor.py           # Modelo do visitante
│   ├── routes/                   # Rotas da API
│   │   ├── __init__.py
│   │   ├── auth.py              # Rotas de autenticação
│   │   └── visitor.py           # Rotas de visitantes
│   ├── static/                   # Arquivos estáticos do frontend
│   │   ├── assets/              # CSS e JS buildados
│   │   ├── index.html           # Página principal
│   │   └── favicon.ico          # Ícone da aplicação
│   └── database/                 # Banco de dados SQLite
│       └── visitors.db          # Arquivo do banco (criado automaticamente)
├── requirements.txt              # Dependências Python
├── Dockerfile                    # Configuração Docker
├── .dockerignore                # Arquivos ignorados pelo Docker
└── README.md                    # Documentação do projeto
```

## 🔌 API Endpoints

### Autenticação

#### POST `/api/auth/login`
Realiza login do administrador.

**Request Body:**
```json
{
  "email": "admin@igreja.com",
  "password": "admin123"
}
```

**Response (200):**
```json
{
  "message": "Login realizado com sucesso",
  "user": {
    "id": 1,
    "email": "admin@igreja.com"
  }
}
```

#### GET `/api/auth/me`
Verifica se o usuário está autenticado.

**Response (200):**
```json
{
  "user": {
    "id": 1,
    "email": "admin@igreja.com"
  }
}
```

#### POST `/api/auth/logout`
Realiza logout do administrador.

**Response (200):**
```json
{
  "message": "Logout realizado com sucesso"
}
```

### Visitantes

#### POST `/api/visitors`
Registra um novo visitante.

**Request Body:**
```json
{
  "nome": "João Silva",
  "telefone": "11999999999",
  "idade": 35,
  "consentimento": true
}
```

**Response (201):**
```json
{
  "message": "Visitante registrado com sucesso",
  "visitor": {
    "id": 1,
    "nome": "João Silva",
    "telefone": "11999999999",
    "idade": 35,
    "consentimento": true,
    "status": "novo",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

#### GET `/api/visitors`
Lista todos os visitantes (requer autenticação).

**Query Parameters:**
- `search` (opcional): Busca por nome ou telefone

**Response (200):**
```json
{
  "visitors": [
    {
      "id": 1,
      "nome": "João Silva",
      "telefone": "11999999999",
      "idade": 35,
      "consentimento": true,
      "status": "novo",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

#### GET `/api/visitors/stats`
Retorna estatísticas dos visitantes (requer autenticação).

**Response (200):**
```json
{
  "total": 10,
  "this_week": 3,
  "new_contacts": 5
}
```

## 🐳 Deploy com Docker

### Build da Imagem

```bash
# Build da imagem Docker
docker build -t visitor-registration .

# Execute o container
docker run -p 5000:5000 visitor-registration
```

### Docker Compose (Opcional)

Crie um arquivo `docker-compose.yml`:

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./src/database:/app/src/database
    environment:
      - FLASK_ENV=production
```

Execute com:
```bash
docker-compose up -d
```

### Deploy em Produção

Para deploy em produção, considere:

1. **Variáveis de Ambiente**:
   - Configure credenciais administrativas via variáveis de ambiente
   - Use um banco de dados mais robusto (PostgreSQL, MySQL)

2. **Servidor WSGI**:
   - Use Gunicorn ou uWSGI em vez do servidor de desenvolvimento do Flask
   - Configure um proxy reverso (Nginx)

3. **Segurança**:
   - Configure HTTPS
   - Use senhas fortes
   - Implemente rate limiting
   - Configure backup do banco de dados

### Exemplo com Gunicorn

```bash
# Instale o Gunicorn
pip install gunicorn

# Execute em produção
gunicorn --bind 0.0.0.0:5000 --workers 4 src.main:app
```


## 🔧 Troubleshooting

### Problemas Comuns

#### Erro de Porta em Uso
```bash
# Encontre o processo usando a porta 5000
lsof -i :5000

# Termine o processo
kill -9 <PID>
```

#### Erro de Dependências Python
```bash
# Atualize o pip
pip install --upgrade pip

# Reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

#### Banco de Dados Corrompido
```bash
# Remova o banco existente (CUIDADO: perderá os dados)
rm src/database/visitors.db

# Reinicie a aplicação para recriar o banco
python src/main.py
```

#### Problemas de CORS
Se encontrar erros de CORS, verifique se:
- O Flask-CORS está instalado
- As configurações de CORS estão corretas no `main.py`
- O frontend está fazendo requisições para a URL correta

### Logs e Debugging

Para habilitar logs detalhados:

```python
# Em src/main.py, adicione:
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contribuição

### Como Contribuir

1. **Fork o projeto**
2. **Crie uma branch para sua feature** (`git checkout -b feature/AmazingFeature`)
3. **Commit suas mudanças** (`git commit -m 'Add some AmazingFeature'`)
4. **Push para a branch** (`git push origin feature/AmazingFeature`)
5. **Abra um Pull Request**

### Padrões de Código

- **Python**: Siga a PEP 8
- **JavaScript**: Use ESLint e Prettier
- **Commits**: Use mensagens descritivas em português
- **Documentação**: Mantenha o README atualizado

### Roadmap de Melhorias

#### Funcionalidades Futuras
- [ ] Sistema de notificações por WhatsApp
- [ ] Relatórios avançados com gráficos
- [ ] Integração com sistemas de CRM
- [ ] App mobile nativo
- [ ] Sistema de check-in com QR Code
- [ ] Múltiplas igrejas/organizações
- [ ] Backup automático na nuvem

#### Melhorias Técnicas
- [ ] Testes automatizados (pytest, Jest)
- [ ] CI/CD com GitHub Actions
- [ ] Monitoramento e métricas
- [ ] Cache com Redis
- [ ] API GraphQL
- [ ] Websockets para atualizações em tempo real

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para suporte técnico ou dúvidas:

- **Email**: suporte@igreja.com
- **Documentação**: Consulte este README
- **Issues**: Use o sistema de issues do GitHub

## 🙏 Agradecimentos

- **React Team**: Pela excelente biblioteca de UI
- **Flask Team**: Pelo framework web simples e poderoso
- **Tailwind CSS**: Pelo framework CSS utilitário
- **Lucide**: Pelos ícones modernos e consistentes
- **Comunidade Open Source**: Por todas as ferramentas utilizadas

---

**Desenvolvido com ❤️ para facilitar o acolhimento de visitantes em igrejas e organizações religiosas.**

## 📊 Status do Projeto

- ✅ **Frontend**: Completo e funcional
- ✅ **Backend**: APIs implementadas e testadas
- ✅ **Banco de Dados**: Configurado e operacional
- ✅ **Autenticação**: Sistema seguro implementado
- ✅ **Deploy**: Dockerizado e pronto para produção
- ✅ **Documentação**: Completa e atualizada
- ✅ **Testes**: Validação manual completa

**Versão Atual**: 1.0.0  
**Última Atualização**: Agosto 2025

#   t e s t e _ v i s i t a n t e s  
 