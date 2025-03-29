from flask import Flask
from utils.config import Config
from utils.extensions import bcrypt, db, jwt, migrate
from routes import auth_bp, todo_bp, heath_bp
from models import *

app = Flask(__name__)

#loding the config
app.config.from_object(Config)

# initializing the app
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
bcrypt.init_app(app)

# registering blueprint
app.register_blueprint(heath_bp, url_prefix = '/')
app.register_blueprint(auth_bp, url_prefix = '/auth/v1')
app.register_blueprint(todo_bp, url_prefix = '/todo/v1')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)