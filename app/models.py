from . import db
import datetime

class Person(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(100), unique=True)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(80), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self ,pid,fname,lname,bio,sex,age,image,created_on):
        self.pid=pid
        self.fname = fname
        self.lname = lname
        self.bio = bio
        self.sex = sex
        self.age = age
        self.image = image
        self.created_on = created_on

    def __repr__(self):
        username=self.fname+' '+self.lname
        return '<Person %r>' % username