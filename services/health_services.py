from flask import jsonify

class HealthService:
    
    @staticmethod
    def index():
        return jsonify({"message":"Hi There! App is working fine !"})