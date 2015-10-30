from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(Form):
    userlogin = StringField('login', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class TestMongoForm(Form):
    opros_id = StringField('opros_id', validators=[DataRequired()])
    gorodm18 = IntegerField('gorodm18', validators=[DataRequired()])
    gorodm30 = IntegerField('gorodm30', validators=[DataRequired()])
    gorodm59 = IntegerField('gorodm59', validators=[DataRequired()])
    gorodm60 = IntegerField('gorodm60', validators=[DataRequired()])
    gorodw18 = IntegerField('gorodw18', validators=[DataRequired()])
    gorodw30 = IntegerField('gorodw30', validators=[DataRequired()])
    gorodw59 = IntegerField('gorodw59', validators=[DataRequired()])
    gorodw60 = IntegerField('gorodw60', validators=[DataRequired()])
    rayonm18 = IntegerField('rayonm18', validators=[DataRequired()])
    rayonm30 = IntegerField('rayonm30', validators=[DataRequired()])
    rayonm59 = IntegerField('rayonm59', validators=[DataRequired()])
    rayonm60 = IntegerField('rayonm60', validators=[DataRequired()])
    rayonw18 = IntegerField('rayonw18', validators=[DataRequired()])
    rayonw30 = IntegerField('rayonw30', validators=[DataRequired()])
    rayonw59 = IntegerField('rayonw59', validators=[DataRequired()])
    rayonw60 = IntegerField('rayonw60', validators=[DataRequired()])
    selom18 = IntegerField('selom18', validators=[DataRequired()])
    selom30 = IntegerField('selom30', validators=[DataRequired()])
    selom59 = IntegerField('selom59', validators=[DataRequired()])
    selom60 = IntegerField('selom60', validators=[DataRequired()])
    selow18 = IntegerField('selow18', validators=[DataRequired()])
    selow30 = IntegerField('selow30', validators=[DataRequired()])
    selow59 = IntegerField('selow59', validators=[DataRequired()])
    selow60 = IntegerField('selow60', validators=[DataRequired()])
    code_gorod = IntegerField('selow60', validators=[DataRequired()])
    code_rayon = IntegerField('selow60', validators=[DataRequired()])
    code_selo = IntegerField('selow60', validators=[DataRequired()])
    code_woman = IntegerField('selow60', validators=[DataRequired()])
    code_man = IntegerField('selow60', validators=[DataRequired()])
    code_18 = IntegerField('selow60', validators=[DataRequired()])
    code_30 = IntegerField('selow60', validators=[DataRequired()])
    code_59 = IntegerField('selow60', validators=[DataRequired()])
    code_60 = IntegerField('selow60', validators=[DataRequired()])
