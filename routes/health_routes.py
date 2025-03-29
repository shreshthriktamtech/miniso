from flask import Blueprint, jsonify
from services import HealthService

heath_bp = Blueprint('health',__name__)

@heath_bp.route('/', methods = ['GET'])
def index():
    return HealthService.index()
