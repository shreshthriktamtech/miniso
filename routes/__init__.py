from routes.auth_routes import auth_bp
from routes.health_routes import heath_bp
from routes.todo_routes import todo_bp

bp = [auth_bp, heath_bp, todo_bp]