from utils.extensions import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    is_active = db.Column(db.Boolean, default = True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates = 'todos')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
    @classmethod
    def create_todo(cls, name, user_id):
        new_todo = cls(name = name, user_id = user_id)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo
    
    @classmethod
    def get_todos(cls, user_id):
        return cls.query.filter_by(user_id = user_id).all()
    

    @classmethod
    def get_todo(cls, id, user_id):
        return cls.query.filter_by(id = id, user_id = user_id).first()
    
