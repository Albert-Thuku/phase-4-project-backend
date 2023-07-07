from flask import Flask, request, make_response, jsonify, json
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Animal, Centre, User, Adoption

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    return {"message" : "Welcome to RescueMePets API"}

class Animals(Resource):

    def get(self):
        animals = [animal.to_dict() for animal in Animal.query.all()]

        if not animals:
            response_body = {"Message" : "Loading animals data....."}
            response = make_response(jsonify(response_body), 404)
            return response
        
        response = make_response(jsonify(animals), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def post(self):
        new_animal = Animal(**request.get_json())   
        db.session.add(new_animal)
        db.session.commit()

        response = make_response(jsonify(new_animal.to_dict()), 201)
        response.headers["Content-Type"] = "application/json"
        return response

api.add_resource(Animals, '/animals')

class AnimalsByID(Resource):

    def get(self,id):
        animal = Animal.query.filter_by(id=id).first()

        if not animal:
            response = make_response(jsonify({"Error" : f"Animal {id} not found"}), 404)
            return response
        
        response = make_response(jsonify(animal.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def patch(self, id):
        animal = Animal.query.filter_by(id=id).first()
        data = request.get_json()  

        for attr, value in data.items():
            setattr(animal, attr, value)

        db.session.add(animal)
        db.session.commit()

        response = make_response(jsonify(animal.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def delete(self,id):
        animal = Animal.query.filter_by(id=id).first()
        db.session.delete(animal)
        db.session.commit()

        response = make_response(jsonify({"Message" : f"Animal {self.name} has been deleted"}), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    
api.add_resource(AnimalsByID, '/animals/<int:id>')

    
class Centres(Resource):

    def get(self):
        centres = [centre.to_dict() for centre in Centre.query.all()]

        if not centres:
            response_body = {"Message" : "Loading centres data....."}
            response = make_response(jsonify(response_body), 404)
            return response
        
        response = make_response(jsonify(centres), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def post(self):
        new_centre = Centre(**request.get_json())   
        db.session.add(new_centre)
        db.session.commit()

        response = make_response(jsonify(new_centre.to_dict()), 201)
        response.headers["Content-Type"] = "application/json"
        return response

api.add_resource(Centres, '/centres')

class CentresByID(Resource):

    def get(self,id):
        centre = Centre.query.filter_by(id=id).first()

        if not centre:
            response = make_response(jsonify({"Error" : f"Centre {id} not found"}), 404)
            return response
        
        response = make_response(jsonify(centre.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def patch(self, id):
        centre = Centre.query.filter_by(id=id).first()
        data = request.get_json()  

        for attr, value in data.items():
            setattr(centre, attr, value)

        db.session.add(centre)
        db.session.commit()

        response = make_response(jsonify(centre.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def delete(self,id):
        centre = Centre.query.filter_by(id=id).first()
        db.session.delete(centre)
        db.session.commit()

        response = make_response(jsonify({"Message" : f"Centre {self.name} has been deleted"}), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    
api.add_resource(CentresByID, '/centres/<int:id>')


class Users(Resource):

    def get(self):
        users = [user.to_dict() for user in User.query.all()]

        if not users:
            response_body = {"Message" : "Loading users data....."}
            response = make_response(jsonify(response_body), 404)
            return response
        
        response = make_response(jsonify(users), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def post(self):
        new_user = User(**request.get_json())   
        db.session.add(new_user)
        db.session.commit()

        response = make_response(jsonify(new_user.to_dict()), 201)
        response.headers["Content-Type"] = "application/json"
        return response

api.add_resource(Users, '/users')

class UsersByID(Resource):

    def get(self,id):
        user = User.query.filter_by(id=id).first()

        if not user:
            response = make_response(jsonify({"Error" : f"User {id} not found"}), 404)
            return response
        
        response = make_response(jsonify(user.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        data = request.get_json()  

        for attr, value in data.items():
            setattr(user, attr, value)

        db.session.add(user)
        db.session.commit()

        response = make_response(jsonify(user.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def delete(self,id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        response = make_response(jsonify({"Message" : f"User {self.name} has been deleted"}), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    
api.add_resource(UsersByID, '/users/<int:id>')


class Adoptions(Resource):

    def get(self):
        adoptions = [adoption.to_dict() for adoption in Adoptions.query.all()]

        if not adoptiona:
            response_body = {"Message" : "Loading adoptions data....."}
            response = make_response(jsonify(response_body), 404)
            return response
        
        response = make_response(jsonify(adoptions), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def post(self):
        new_adoption = Adoption(**request.get_json())   
        db.session.add(new_adoption)
        db.session.commit()

        response = make_response(jsonify(new_adoption.to_dict()), 201)
        response.headers["Content-Type"] = "application/json"
        return response

api.add_resource(Adoptions, '/adoptions')

class AdoptionsByID(Resource):

    def get(self,id):
        adoption = Adoption.query.filter_by(id=id).first()

        if not adoption:
            response = make_response(jsonify({"Error" : f"Adoption {id} not found"}), 404)
            return response
        
        response = make_response(jsonify(adoption.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def patch(self, id):
        adoption = Adoption.query.filter_by(id=id).first()
        data = request.get_json()  

        for attr, value in data.items():
            setattr(adoption, attr, value)

        db.session.add(adoption)
        db.session.commit()

        response = make_response(jsonify(adoption.to_dict()), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    
    def delete(self,id):
        adoption = Adoption.query.filter_by(id=id).first()
        db.session.delete(adoption)
        db.session.commit()

        response = make_response(jsonify({"Message" : f"Adoption {self.id} has been deleted"}), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    
api.add_resource(AdoptionsByID, '/adoptions/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)