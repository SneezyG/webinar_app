import os
import requests
from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func, or_
from models import *

config = {
    "DEBUG": True,          
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgres://ghbyddgfalkoor:1b673118eda5373eb5294e2e0531d5d6a9fcd24873623f2b8dd9b4a5321ae019@ec2-34-234-228-127.compute-1.amazonaws.com:5432/d3ei12t3hp8l6p")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config.from_mapping(config)
cache = Cache(app)

db.init_app(app)


@cache.cached(timeout=300)
@app.route("/")
def registrationpage():
    return render_template("registration.html")
    

@app.route("/registration")
def registration():    
     name = request.form.get("name")
     nationality = request.form.get("nationality")
     sex = request.form.get("sex")
     age = request.form.get("age")
     email = request.form.get("email")
     occupation = request.form.get("occupation")
    
     user  = User_tutor(name=name, nationality=nationality, sex=sex, age=age, email=email, occupation=occupation)
     db.session.add(user)
     db.session.commit()
     return render_template("success.html")
     
  
