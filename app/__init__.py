# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import _mysql_connector

app = Flask(__name__)
app.config['SECRET_KEY'] = '123SCMkusinlaite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Scm211-0204/2019@localhost/messaging'
db = SQLAlchemy(app)
api = Api(app)
