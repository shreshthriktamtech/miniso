from flask import jsonify

class TodoService:
    @staticmethod
    def getTodos(data):
        return jsonify({"message":"sa"})