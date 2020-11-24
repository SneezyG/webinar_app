import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User_tutor(db.Model):
    __tablename__ = "users_tutor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    sex = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)