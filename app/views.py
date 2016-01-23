# -*- coding: utf-8 -*-
from flask import render_template, redirect, jsonify, request
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from .login import User
from .forms import LoginForm
from .storeboatssql import Store
from app import app

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


@app.route('/boatssave', methods=['POST'])
def boatssave():
    data = request.data
    b = Store()
    b.saveboats(data)
    return data
