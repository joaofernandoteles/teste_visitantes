# 🚀 Guia de Início Rápido

## Executar o Sistema (3 passos)

### 1. Instalar Dependências
```bash
cd visitor-registration-backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Executar a Aplicação
```bash
python src/main.py
```

### 3. Acessar o Sistema
- **Site**: http://localhost:5000
- **Admin**: http://localhost:5000/admin
- **Login**: admin@igreja.com / admin123

## 🐳 Executar com Docker (1 passo)

```bash
docker build -t visitor-registration .
docker run -p 5000:5000 visitor-registration
```

## ✨ Funcionalidades Principais

- ✅ **Registro de Visitantes**: Formulário simples e intuitivo
- ✅ **Dashboard Admin**: Estatísticas e gerenciamento completo
- ✅ **Busca e Exportação**: Localizar e exportar dados em CSV
- ✅ **Design Responsivo**: Funciona em desktop e mobile
- ✅ **Sistema Integrado**: Frontend + Backend em uma aplicação

## 📱 Como Usar

### Para Visitantes
1. Acesse http://localhost:5000
2. Preencha o formulário de registro
3. Clique em "Fazer parte"

### Para Administradores
1. Acesse http://localhost:5000/admin
2. Faça login com admin@igreja.com / admin123
3. Visualize estatísticas e gerencie registros

## 🔧 Personalização Rápida

### Alterar Credenciais Admin
Edite `src/main.py`, linha ~45:
```python
admin_user = User(email='seu@email.com', password='suasenha')
```

### Alterar Textos da Interface
Edite os arquivos em `src/static/` após fazer novo build do frontend.

### Alterar Cores
As cores estão definidas no Tailwind CSS (azul como cor principal).

## 📞 Suporte

- **Documentação Completa**: Veja `README.md`
- **Problemas**: Verifique a seção Troubleshooting no README
- **Logs**: Execute com `python src/main.py` para ver logs detalhados

