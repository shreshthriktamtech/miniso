from flask import jsonify
from models import User
from flask_jwt_extended import jwt_required, get_jwt_identity

class AuthService:

    @staticmethod
    def login(data):
        if 'email' not in data or 'password' not in data:
            return jsonify({"message": "All fields are required"}), 400
        
        user:User = User.find_by_email(email=data['email'])

        if user is None:
            return jsonify({"message": "Invalid Email or Password"}), 400
        
        if not user.check_password(data['password']):
            return jsonify({"message": "Invalid Email or Password"}), 400
        
        user_data = {
            "token": user.generate_token()
        }

        return jsonify({"message":"login successful", "data": user_data})
    
    @staticmethod
    def register(data):

        if 'name' not in data or 'password' not in data or 'email' not in data:
            return jsonify({"message": "All fields are required"}), 400
        
        existing_user: User = User.find_by_email(data['email'])
        if existing_user:
            return jsonify({"message": "Email already exist"}), 400
        

        user: User = User.create_user(data['name'], data['email'], data['password'])
        
        user_data = {
            "user": user.to_dict(),
            "token": user.generate_token()
        }
        return jsonify({"message": "User created successfully", "data": user_data})
    
    @staticmethod
    @jwt_required()
    def get_user():
        identity = get_jwt_identity()
        print(identity)
        user: User = User.find_by_id(identity)
        return jsonify({"message": "user", "data": user.to_dict()})

        