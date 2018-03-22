"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""


import os
from flask import session,render_template, request, redirect, url_for, jsonify,flash
SECRET_KEY="super secure key"
from random import randint
from werkzeug.utils import secure_filename
from app.models import Person
from sqlalchemy.sql import exists
from datetime import *
from app import app,db
import time
from form import Pform
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile/',methods=['GET','POST'])
def profile_add():
    form = Pform(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            bio = request.form['bio'].strip()
            fname = request.form['fname'].strip()
            lname = request.form['lname'].strip()
            gender = request.form['gender']
            age = request.form['age']
            image = request.files['image']
            while True:
                numid = randint(450000,470000)
                pid = 'PID'+ str(numid)
                if not db.session.query(exists().where(Person.pid == str(pid))).scalar():
                    break
            filename = secure_filename(image.filename)
            image.save(os.path.join('app/static/Images', filename))
            created_on = datetime.now()
            person = Person(pid,fname,lname,bio,sex,age,filename,created_on)
            db.session.add(person)
            db.session.commit()
            flash("Database Updated: New Account")
            return redirect('/profiles')
    return render_template('profile_form.html',form=form)

@app.route('/profile/<pid>', methods=['POST', 'GET'])
def selectedprofile(pid):
  person = Person.query.filter_by(pid=pid).first()
  if not person:
      flash("Error: User Not Found" )
  else:
      image = '/static/Images/' + person.image
      if request.method == 'POST' and request.headers['Content-Type']== 'application/json':
            return jsonify(pid=person.pid, image=image,username=person.fname+' '+person.lname, gender=person.gender,bio=person.bio, age=person.age,created_on=person.created_on)
      else:
            person = {'ID':person.pid,'image':image, 'username':person.fname+' '+person.lname,'fname':person.fname, 'lname':person.lname,'bio':person.bio,'age':person.age, 'gender':person.gender,'created_on':person.created_on}
            return render_template('profile.html', person=person)
  return redirect(url_for("profiles"))


@app.route('/profiles', methods=["GET", "POST"])
def profiles():
  persons = db.session.query(Person).all()
  lst=[]
  for person in persons:
    lst.append({'username':person.fname+' '+person.lname,'pid':person.pid})
    if request.method == 'POST' and request.headers['Content-Type']== 'application/json':
        return jsonify(persons=lst)
  return render_template('profiles.html', persons=persons)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="5000")
