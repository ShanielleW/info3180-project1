from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "megasecure key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:pass@localhost/project "
db = SQLAlchemy(app)
from app import views
from app.models import Person
