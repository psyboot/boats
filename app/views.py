# -*- coding: utf-8 -*-
from flask import render_template, redirect
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from .login import User
from .forms import LoginForm
from app import app

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    return redirect('/login')


@app.route('/')
@login_required
def root():
    return "Root!"


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        remember_me = str(form.remember_me.data)
        user_entry = User.get(login)
        if (user_entry is not None):
            user = User(user_entry[0],user_entry[1])
            if (user.password == password):
                login_user(user)
                return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/index')
def index():
    #fake database
    user = {'login': 'nick'}

    boats = [
    {
        "name": u"Николай Иванов",
        "number": "1234",
        "sea": False
    },
    {
        "name": u"Анна Зайцева",
        "number": "54321",
        "sea": True
    },
    {
        "name": u"Петр Сидоров",
        "number": "153215",
        "sea": True
    }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        boats = boats)
