# -*- coding: utf-8 -*-
from flask import render_template, redirect, jsonify, request, flash, url_for, g, session
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from .login import User
from .forms import LoginForm, SaveBoats
from .storeboatssql import Store
from .log import Log
from app import app, db, models
import json
import datetime

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = {} 
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        remember_me = str(form.remember_me.data)
        user_entry = User.get(login)
        if (user_entry is not None):
            user = User(user_entry[0], user_entry[1])
            if (user.password == password):
                login_user(user)
                return redirect(url_for('root'))
        errors['namepass'] = u'Неправильно введено имя пользователя или пароль.'
        errors['fields'] = u'Заполните все поля.'
        return render_template('login.html',
                               title='Sign In',
                               errors=errors,
                               form=form)
    return render_template('login.html',
                           title="Login.",
                           errors=errors,
                           form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('root'))


@login_manager.user_loader
def load_user(userid):
    u = User.get(userid)
    print(u)


@app.route('/')
@login_required
def root():
    print ("authenticated:", current_user.is_authenticated)  # debug
    stboats = Store()
    stboats.loadboatssql()
    return render_template('indexangular.html',
                           title='Boats!', insea=stboats.insea,
                           notinsea=stboats.notinsea)


@app.route('/boatsjson')
def boatsjson():
    b = Store()
    b.loadboats()
    return jsonify(boats=b.boatsjson[0], seaornot=b.boatsjson[1])


@app.route('/boatssql')
def boatssql():
    b = Store()
    b.loadboatssql()
    # print ("b: ",b.boatsjson[0])
    boatsjs = ""
    seaornotjs = ""
    if(b.boatsjson):
        boatsjs = b.boatsjson[0]
        seaornotjs = b.boatsjson[1]
    return jsonify(boats=boatsjs, seaornot=seaornotjs)


@app.route('/boatsadd', methods=['GET', 'POST'])
def boatsadd():
    # Пускаем только админа
    if (('user_id' in session) and (session['user_id'] != 'admin')):
        return redirect(url_for('root'))
    errors = {}
    form = SaveBoats()
    b = Store()
    b.loadboatssql()
    if form.validate_on_submit():
        double_name = db.session.query(models.Boats).filter_by(
            name=form.name.data).first()
        double_number = db.session.query(models.Boats).filter_by(
            number=form.number.data).first()
        if (double_name or double_number):
            if double_name:
                errors['name'] = u"Ошибка! Такое имя есть в базе."
            if double_number:
                errors['number'] = u"Ошибка! Такой номер есть в базе."
            return render_template('editboats.html', title='Add boat',
                                   boats=b.boatsjson[0], form=form,
                                   errors=errors)
        boats = models.Boats(name=form.name.data, number=form.number.data,
                             pier=form.pier.data,
                             license=form.license.data, sea=False)
        try:
            db.session.add(boats)
            db.session.commit()
            return redirect(url_for('boatsadd'))
        except Exception as e:
            flash(e)
    boatsjs = ""
    if(b.boatsjson):
        boatsjs = b.boatsjson[0]
    return render_template('editboats.html', title='Add boat',
                           boats=boatsjs, form=form, errors=errors)


@app.route('/delete/', methods=['GET'])
def delete():
    # Пускаем только админа
    if (('user_id' in session) and (session['user_id'] != 'admin')):
        return redirect(url_for('root'))
    db.session.query(models.Boats).filter_by(
        name=request.args.get('name')).delete()
    db.session.commit()
    return redirect(url_for('boatsadd'))


@app.route('/edit/', methods=['GET', 'POST'])
def edit():
    # Пускаем только админа
    if (('user_id' in session) and (session['user_id'] != 'admin')):
        return redirect(url_for('root'))
    errors = {}
    form = SaveBoats()
    name = request.args.get('name')
    number = request.args.get('number')
    pier = request.args.get('pier')
    license = request.args.get('license')
    id_ = db.session.query(models.Boats).filter_by(name=form.name.data).first()
    if form.validate_on_submit():
        try:
            db.session.query(models.Boats).filter_by(id=id_.id).update(
                {"number": form.number.data, "name": form.name.data,
                 "pier": form.pier.data, "license": form.license.data})
            db.session.commit()
            return redirect(url_for('boatsadd'))
        except Exception as e:
            flash(e)
    return render_template('editsingleboat.html', title='Edit boat', name=name,
                           number=number, pier=pier, license=license,
                           form=form, errors=errors)


@app.route('/boatssave', methods=['POST'])
def boatssave():
    data = request.get_json()
    name = data['name']
    number = data['number']
    pier = data['pier']
    license = data['license']
    id_ = db.session.query(models.Boats).filter_by(number=number).first()
    try:
        db.session.query(models.Boats).filter_by(
            id=id_.id).update({"sea": data['sea']})
    except Exception as e:
        flash(e)
    if(data['sea']):
        # statetxt = str(app.config('FROM'))
        statetxt = u"Вышла со стоянки."
    else:
        # statetxt = app.config('IN')
        statetxt = u"Пришла на стоянку."
    # state = models.SeaChanged(state=statetxt, number=number, datechanged=datetime.datetime.now())
    # db.session.add(state)
    # db.session.commit()
    logline = str(datetime.datetime.now().strftime(
        '%d.%m.%y  %H:%M')) + u': Лодка ' + number + ' ' + statetxt
    print "logline: ", logline
    log = Log()
    log.log(session['user_id'], logline)
    return redirect(url_for('root'))


@app.route('/log', methods=['POST', 'GET'])
def log():
    datalog = db.session.query(models.SeaChanged).all()
    print " ".join(datalog)
    return " ".join(datalog)

@app.route('/getlogs', methods=['POST', 'GET'])
def getlogs():
    logs = Log()
    logfiles = logs.getlogs()
    return render_template('showlogs.html', title='Logs', logfiles=logfiles)
