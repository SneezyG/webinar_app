import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgres://ghbyddgfalkoor:1b673118eda5373eb5294e2e0531d5d6a9fcd24873623f2b8dd9b4a5321ae019@ec2-34-234-228-127.compute-1.amazonaws.com:5432/d3ei12t3hp8l6p")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()
    
if __name__ == "__main__":
    with app.app_context():
        main()