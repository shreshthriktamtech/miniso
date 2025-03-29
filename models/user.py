from utils.extensions import bcrypt, db
from datetime import datetime
from flask_jwt_extended import create_access_token

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), unique = True ,nullable = False)
    password = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #relations
    todos = db.relationship("Todo", back_populates = 'user', cascade="all, delete-orphan")
    # Methods
    def set_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return bcrypt.check_password_hash(self.password, password)
    
    def generate_token(self):
        """Checks if the provided password matches the stored hash."""
        return create_access_token(identity=str(self.id))
    
    def to_dict(self):
        """return the dict"""
        return {
            "id": self.id, 
            "name": self.name,
            "email": self.email,
        }

    # class methods
    @classmethod
    def find_by_email(cls, email):
        """Finds a user by email."""
        return cls.query.filter_by(email=email).first()
    
        # class methods
    @classmethod
    def find_by_id(cls, id):
        """Finds a user by id."""
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all_users(cls):
        """get all users"""
        return cls.query.all()
    
    @classmethod
    def create_user(cls, name, email, password):
        existing_user = cls.find_by_email(email)
        if existing_user:
            raise ValueError("User with this email already exists") 
        new_user = cls(name = name, email = email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

