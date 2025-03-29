from flask import Blueprint, jsonify, request
from services import TodoService


todo_bp = Blueprint('todo',__name__)

@todo_bp.route('/', methods = ['GET'])
def get_todos():
    try:
        return TodoService.get_todos()
    except Exception as e:
        print(str(e))
        return jsonify({"message": "Opps Something went wrong!"}), 400
    

@todo_bp.route('/add', methods = ['POST'])
def add_todo():
    try:
        print("sa")
        data = request.get_json()
        print(data)
        return TodoService.add_todo(data)
    except Exception as e:
        print(str(e))
        return jsonify({"message": "Opps Something went wrong!"}), 400
    
