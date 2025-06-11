from flask_restful import Resource
from models import my_users


class UserResource(Resource):
    def get(self, id):
        users = my_users.query.filter_by(id=id).first()
        return users
    
    def post(self):
        return {"message":"user added"}

    def delete(self, id):
        return{"message":"user deleted"}