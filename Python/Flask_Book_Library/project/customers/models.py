from project import db, app
import re
from sqlalchemy.orm import validates


# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    _TEXT = re.compile(r"[\w\s.,'\-:!?()]{1,64}")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    @validates('name', 'city')
    def _validate_text(self, key, value):
        if value is None or value == '':
            if key == 'name':
                raise ValueError(f'Invalid {key}')
            return value
        if not isinstance(value, str) or not self._TEXT.fullmatch(value):
            raise ValueError(f'Invalid {key}')
        return value

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"


with app.app_context():
    db.create_all()
