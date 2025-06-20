from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate
from methods.users import UserResource
from methods.categories import CategoriesResource
# from methods.budgets import BudgetResource
# from methods.expenses import ExpenseResource
from models import db

app = Flask(__name__)

api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"

app.config["SQLALCHEMY_ECHO"] = True

migrate= Migrate(app, db)

db.init_app(app)



# Get "/"
@app.route("/")
def index():
    return[]

# # Get a user
# @app.route("/users/<id>", methods=["GET"])
# def get_user(id):
#     return {"message": f"User {id} retrieved"}

# # Add a user
# @app.post("/users")
# def add_user():
#     return{"massage": "user added"}

# # Delete user
# @app.delete("/users/<id>")
# def delete_user(id):
#     return{"message":"user deleted"}

# # Get categories
# @app.get("/categories")
# def get_categories():
#     return []

# # Add an expense category
# @app.post("/categories")
# def add_category():
#     return{"message":"category added"}

# # Delete an expense category
# @app.delete("/categories/<id>")
# def delete_category(id):
#     return {"message": "category deleted"}

# # Get budgets
# @app.get("/budgets")
# def get_budget():
#     return []

# # Add a budget 
# @app.post("/budgets")
# def add_budget():
#     return {"message":"budget added"}

# # Delete a budget
# @app.delete("/budgets/<id>")
# def delete_budget(id):
#     return{"message":"budget deleted"}

# # Update a budget
# @app.patch("/budgets/<id>")
# def update_budget(id):
#     return {"message":"budget updated"}

# # Get expenses
# @app.get("/expenses")
# def get_expenses():
#     return []

# # Add an expense
# @app.post("/expenses")
# def add_expense():
#     return{"message":"added expense"}

# # Delete an expense
# @app.delete("/expenses/<id>")
# def delete_expense(id):
#     return{"messsage":"expense deleted"}

# # Update an expense
# @app.patch("/expenses/<id>")
# def update_expense(id):
#     return {"message":"updated expense"}
    
api.add_resource(UserResource, "/users", "/users/<id>")
api.add_resource(CategoriesResource, "/categories", "/categories/<id>")
# api.add_resource(BudgetResource, "/budgets", "/budgets/<id>")
# api.add_resource(ExpenseResource, "/expenses", "/expenses/<id>")