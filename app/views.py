# -*- coding: utf-8 -*-
from flask import render_template, redirect, jsonify, request, flash, url_for
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from .login import User
from .forms import LoginForm, SaveBoats
from .storeboatssql import Store
from app import app, db, models

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    return redirect('/login')


@app.route('/')
# @login_required
def root():
    stboats = Store()
    stboats.loadboatssql()
    return render_template('indexangular.html',
                           title='Boats!', insea=stboats.insea, notinsea=stboats.notinsea)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        remember_me = str(form.remember_me.data)
        user_entry = User.get(login)
        if (user_entry is not None):
            user = User(user_entry[0], user_entry[1])
            if (user.password == password):
                login_user(user)
                return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/index')
def index():
    stboats = Store()
    stboats.loadboats()
    boats = stboats.boatsjson
    return render_template("index.html", title='Home', boats=boats, insea=stboats.insea, notinsea=stboats.notinsea)


@app.route('/boatsjson')
def boatsjson():
    b = Store()
    b.loadboats()
    return jsonify(boats=b.boatsjson[0], seaornot=b.boatsjson[1])


@app.route('/boatssql')
def boatssql():
    b = Store()
    b.loadboatssql()
    return jsonify(boats=b.boatsjson[0], seaornot=b.boatsjson[1])


@app.route('/boatsadd', methods=['GET', 'POST'])
def boatsadd():
    errors = {}
    form = SaveBoats()
    b = Store()
    b.loadboatssql()
    if form.validate_on_submit():
        double_name = db.session.query(models.Boats).filter_by(name=form.name.data).first()
        double_number = db.session.query(models.Boats).filter_by(number=form.number.data).first()
        if (double_name or double_number):
            if double_name:
                errors['name'] = u"Ошибка! Такое имя есть в базе."
            if double_number:
                errors['number'] = u"Ошибка! Такой номер есть в базе."
            return render_template('editboats.html', title='Add boat',boats=b.boatsjson[0], form=form, errors=errors)
        boats = models.Boats(name=form.name.data, number=form.number.data, sea=False)
        try:
            db.session.add(boats)
            db.session.commit()
            return redirect(url_for('boatsadd'))
        except Exception as e:
            flash(e)
    return render_template('editboats.html', title='Add boat', boats=b.boatsjson[0], form=form, errors=errors)


@app.route('/delete/<name>')
def delete(name):
    db.session.query(models.Boats).filter_by(name=name).delete()
    db.session.commit()
    return redirect(url_for('boatsadd'))


@app.route('/boatssave', methods=['POST'])
def boatssave():
    data = request.data
    b = Store()
    b.saveboats(data)
    return data
