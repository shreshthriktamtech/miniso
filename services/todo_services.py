from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Todo

class TodoService:
    @staticmethod
    @jwt_required()
    def add_todo(data):
        if 'name' not in data:
            return jsonify({"message":"Name is required"}), 400
        
        user_id = get_jwt_identity()
        todo = Todo.create_todo(data['name'], user_id)

        todo_data = {
            "todo": todo.to_dict()
        }

        return jsonify({"message":"Todo Added", "data": todo_data})
    

    @staticmethod
    @jwt_required()
    def get_todos():
        user_id = get_jwt_identity()
        todos_list = Todo.get_todos(user_id)
        todos = [todo.to_dict() for todo in todos_list]
        return jsonify({"message":"Todo List", "data": todos})
    