from flask_restful import Resource
from models import Categories

class CategoriesResource(Resource):
# get the categories
    def get(self):
        categories = Categories.query.all()
        return categories
    
# add a category
    def post(self):
        return{"message":"category added"}
    
# delete a category
    def delete(self, id):
        return {"message":"category deleted"}
