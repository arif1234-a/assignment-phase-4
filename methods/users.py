from flask_restful import Resource
from models import Users


class UserResource(Resource):
    def get(self, id):
        users =Users.query.filter_by(id=id).first()
        return users
    
    def post(self):
        return {"message":"user added"}

    def delete(self, id):
        return{"message":"user deleted"}