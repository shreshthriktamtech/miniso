from flask import Blueprint, jsonify

todo_bp = Blueprint('todo',__name__)

@todo_bp.route('/', methods = ['GET'])
def get_todos():
    return jsonify({"message":"login"})
