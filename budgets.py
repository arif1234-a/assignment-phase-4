from flask_restful import Resource
from models import my_budgets

class BudgetResource(Resource):
# get budgets
    def get (self):
        budgets = my_budgets.query.all()
        return budgets

# add budget
    def post(self):
        return{"message":"budget added"}

# update budget
    def patch(self, id):
        return{"message":"budget updated"}
    
# delete a budget
    def delete(self,id):
        return{"message":"budget removed"}