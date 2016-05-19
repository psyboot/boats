# -*- coding: utf-8 -*-
from flask.ext.login import UserMixin


class User(UserMixin):
    # proxy for a database of users "login": ("Name", "Password")
    user_database = {"nick": (u"Николай", "pass"),
                     "user": (u"Иван Иванов", "user"),
                     "admin": (u"admin", "admin")}

    def __init__(self, username, password):
        self.id = username
        self.password = password

    @classmethod
    def get(cls, id):
        # return cls.user_database.get(id)
        if id in cls.user_database:
            return cls.user_database[id]
        #else:
            #return "anonymous"
