from flask import Flask

app = Flask(__name__)

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

# Add an expense category
@app.post("/categories")
def add_category():
    return{"message":"category added"}

# Delete an expense category
@app.delete("/categories/<id>")
def delete_category(id):
    return {"message": "category deleted"}

# Add a budget 
@app.post("/budget")
def add_budget():
    return {"message":"budget added"}

# Delete a budget
@app.delete("/budget/<id>")
def delete_budget(id):
    return{"message":"budget deleted"}

# Update a budget
@app.patch("/budget/<id>")
def update_budget(id):
    return {"message":"budget updated"}

# Add a 
    