from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms import validators

class LoginForm(Form): #Form : extends form object
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class CreateUserandAOE(Form):
	username = StringField('username', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	profile = StringField('profile', validators=[validators.Length(min=10, max=700), DataRequired()])
	state = StringField('state', validators=[validators.Length(min=2, max=2), DataRequired()])
	city = StringField('city', validators=[validators.Length(min=2, max=100), DataRequired()])
	activity = StringField('activity', validators=[validators.Length(min=2, max=100), DataRequired()])

class Search(Form):
	state = StringField('state', validators=[validators.Length(min=2, max=2), DataRequired()])
	city = StringField('city', validators=[validators.Length(min=2, max=100), DataRequired()])
	activity = StringField('activity', validators=[validators.Length(min=2, max=100), DataRequired()])

