from flask.ext.wtf import Form
from wtforms.fields import TextField,SubmitField,RadioField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required,InputRequired ,NumberRange, ValidationError
from flask_wtf.html5 import IntegerField
from sqlalchemy.sql import exists
from app import db
from app.models import Person



class Pform(Form):
    fname = TextField("FirstName",validators=[Required("Please enter your first name.")])
    lname = TextField("LastName",validators=[Required("Please enter your last name.")])
    bio= TextField("Biography",validators=[Required("Please enter a short biography.")])
    sex = RadioField("Gender",choices=[('Male'),('Female')])
    age = IntegerField('Age', validators=[Required(),NumberRange(min=0, max=100)])
    image = FileField('Profile image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only in format "jpg" and "png"')])
    submit = SubmitField("Submit")