from flask import Blueprint, request, jsonify
from services import AuthService

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/', methods = ['GET'])
def get_user():
    try:
        return AuthService.get_user()
    except Exception as e:
        print(str(e))
        return jsonify({"message": "Opps Something went wrong!"}), 400

@auth_bp.route('/login', methods = ['POST'])
def login():
    try:
        data = request.get_json()
        return AuthService.login(data)
    except Exception as e:
        print(str(e))
        return jsonify({"message": "Opps Something went wrong!"}), 400

@auth_bp.route('/register', methods = ['POST'])
def register():
    try:
        data = request.get_json()
        return AuthService.register(data)
    except Exception as e:
        print(str(e))
        return jsonify({"message": "Opps Something went wrong!"}), 400