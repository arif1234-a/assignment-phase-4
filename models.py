from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Categories (db.Model):
    __tablename__= "categories"

    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.Text, nullable= False)


class Users(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key = True)
    username= db.Column(db.Text, nullable= False)
    email = db.Column(db.Text, nullable= False)

