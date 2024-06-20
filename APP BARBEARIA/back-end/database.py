from flask_sqlalchemy import SQLAlchemy

# Inicializa o SQLAlchemy
db = SQLAlchemy()

# Definição dos modelos de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Pode ser 'funcionario', 'gerente' ou 'admin'

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # Tipo de recurso, como 'equipamento', 'veiculo', etc.
