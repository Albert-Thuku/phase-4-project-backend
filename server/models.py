from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Animal(db.Model, SerializerMixin):
    __tablename__ = 'animals'
    serialize_rules = ('-centre.animals',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    adopted = db.Column(db.Boolean, nullable=False)

    centre_id = db.Column(db.Integer, db.ForeignKey('centres.id'))
    centre = db.relationship('Centre', back_populates='animals')

    def __repr__(self):
        return f'<Animal name {self.name} | adopted: {self.adopted}>'


class Centre(db.Model, SerializerMixin):
    __tablename__ = 'centres'
    serialize_rules = ('-animals.centre',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=True)
    location = db.Column(db.String, unique=True)

    animals = db.relationship('Animal', back_populates='centre', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Centre name {self.name} | location: {self.location}>'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-animals',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30))
    age = db.Column(db.Integer, db.CheckConstraint('age>18'))
    email = db.Column(db.String, db.CheckConstraint('@ in email'))
    password = db.Column(db.String(length=10))
    status = db.Column(db.String)

    def __repr__(self):
        return f'<User name {self.name} | email: {self.email}>'


class Adoption(db.Model, SerializerMixin):
    __tablename__ = 'adoptions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'))
    user = db.relationship('User', back_populates='animals')
    animal = db.relationship('Animal', back_populates='animals')

    def __repr__(self):
        return f'<Adoption id: {self.id}>'
