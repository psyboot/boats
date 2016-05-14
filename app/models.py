#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    boats = db.relationship('Boats', backref='author', lazy='dynamic')
    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Boats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pier = db.Column(db.Integer())  # номер стоянки
    name = db.Column(db.String(140))  # Ф.И.О.
    number = db.Column(db.String(50))  # Судовой номер
    sea = db.Column(db.Boolean, unique=False,
                    default=False)  # В море (True), на причале (False)
    license = db.Column(db.String(50))  # Номер водительского удостоверения
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Boats %r>' % (self.name)


class SeaChanged(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datechanged = db.Column(db.DateTime)  # Дата, когда лодка приходила и выезжала
    state = db.Column(db.String(50))  # Запись о состоянии лодки, например "Пришла в порт", вышла из порта. Брать из config.py
    number = db.Column(db.String(50), db.ForeignKey('boats.number'))  # Номер лодки, которая приходила или уходила

    nickname = db.Column(db.String(64))  # Имя дежурного
