from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('pass', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class SaveBoats(Form):
    name = StringField('name', validators=[DataRequired()])
    number = IntegerField('number', validators=[DataRequired()])
