from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from backend.routes import main_blueprint
from backend.auth import auth_blueprint
from backend.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wayne_industries.db'
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['JWT_SECRET_KEY'] = 'sua_chave_jwt'

# Inicializa a extensão do banco de dados com o aplicativo Flask
db.init_app(app)

# Registra os blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    # Cria as tabelas no banco de dados se elas não existirem
    with app.app_context():
        db.create_all()
    app.run(debug=True)
