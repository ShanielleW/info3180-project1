from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "megasecure key"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ousjpnvxzffiif:3678abed05d99504b205f3f0ce4c841c0b723397d4d7eaa0aa1b35f5d42ade0e@ec2-23-21-217-27.compute-1.amazonaws.com:5432/df9e52d10fl60b"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:pass@localhost/project"
db = SQLAlchemy(app)
from app import views
from app.models import Person
