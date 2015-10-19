from flask.ext.wtf import Form

from wtforms import TextField,BooleanField, SubmitField,TextAreaField, validators, ValidationError

class ContactForm(Form):
  name = TextField("Name",  [validators.Required("Please enter your name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Send")

class Authentification(Form):
	login = TextField("Login",[validators.Required("Please enter your login")])
	password = TextField("Password", [validators.Required("Please enter your password")])
	submit = SubmitField("Send")