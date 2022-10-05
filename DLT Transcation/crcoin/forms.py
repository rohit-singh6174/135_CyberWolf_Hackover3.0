from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class RegistrationForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    email= StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='Sign Up')

class LoginForm(FlaskForm):
    email= StringField(label='Email',validators=[DataRequired(),Email()])
    password=PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=20)])
    submit=SubmitField(label='Login in')

class TransactionForm(FlaskForm):
	sender = StringField('Sender',validators=[DataRequired(), Length(min=4, max=15)]);
	receiver = StringField('Receiver',validators=[DataRequired(), Length(min=4, max=15)]);
	amount = IntegerField('Amount', validators=[DataRequired()]);
	key = StringField('Key', validators=[DataRequired()]);
	dummy = StringField('Dummy');
	submit = SubmitField('Make a Transaction!');