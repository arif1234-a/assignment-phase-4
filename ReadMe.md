# Assignment
-   Come up with any app idea and 3 to 5 models (account for relationships)
-   Create the complete routes routes for each model (C.R.U.D)
-   Create a postman collection of all models plus routes
-   Refactor the flask routes and use flask-restful
Day 3
-  From your previous discussion, pick two models and use flask-sqlalchemy and flask-migrate to create the tables plus columns
-  Create get routes using flask-restful for both models and query the two tables

# The idea
- Personal Finance Tracker
- This app will help users track their expenses and budgets while maintaining clear records.


# Structure 
- 4 Models (User, Expense, Budget , category):
- users
- id: Unique identifier
- username: Name of the user
- email: Contact email

- expenses (Linked to User & Category)
- id: Unique identifier
- user_id: Belongs to a user
- amount: Transaction value
- category_id: Linked to a spending category
- date: When the transaction happened

- categories (Linked to Transactions)
- id: Unique identifier
- name: Example: Food, Rent, Savings, Investment

- budgets (Linked to User & Category)
- id: Unique identifier
- user_id: Belongs to a user
- category_id: Which expense category it applies to
- limit: Max allowed spending in that category

# Relationships:
- One user → Many Expenses
- One transaction/expense → Belongs to one category
- One user → Can set multiple budgets
