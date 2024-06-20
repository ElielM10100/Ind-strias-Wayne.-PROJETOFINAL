from flask import Blueprint, render_template, jsonify
from flask_jwt_extended import jwt_required

from backend.database import Resource

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/dashboard')
@jwt_required()
def dashboard():
    resources = Resource.query.all()
    return render_template('dashboard.html', resources=resources)
