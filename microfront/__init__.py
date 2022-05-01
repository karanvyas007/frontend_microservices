from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'campfood'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/campfood_webapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.config.from_object("config")

from Microfront import routes
