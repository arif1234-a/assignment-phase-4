from flask import Flask

app = Flask(__name__)

# Get "/"
@app.route("/")
def index():
    return{"massage": "welcome to your finance tracker"}

# Get a single user
@app.get("/users/<id>")
def get_user(id):
    return []

# Add a user
@app.post("/users")
def add_user():
    return{"massage": "user added"}

# Delete user
@app.delete("/users/<id>")
def delete_user(id):
    return{"message":"user deleted"}

# Get categories
@app.get("/categories")
def get_categories():
    return []

# Add an expense category
@app.post("/categories")
def add_category():
    return{"message":"category added"}

# Delete an expense category
@app.delete("/categories/<id>")
def delete_category(id):
    return {"message": "category deleted"}

# Get budgets
@app.get("/budgets")
def get_budget():
    return []

# Add a budget 
@app.post("/budgets")
def add_budget():
    return {"message":"budget added"}

# Delete a budget
@app.delete("/budgets/<id>")
def delete_budget(id):
    return{"message":"budget deleted"}

# Update a budget
@app.patch("/budgets/<id>")
def update_budget(id):
    return {"message":"budget updated"}

# Get expenses
@app.get("/expenses")
def get_expenses():
    return []

# Add an expense
@app.post("/expenses")
def add_expense():
    return{"message":"added expense"}

# Delete an expense
@app.delete("/expenses/<id>")
def delete_expense(id):
    return{"messsage":"expense deleted"}

# Update an expense
@app.patch("/expenses/<id>")
def update_expense(id):
    return {"message":"updated expense"}
    