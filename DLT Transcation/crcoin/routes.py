from flask import Flask, render_template, url_for, redirect, flash
from crcoin import app
from crcoin.forms import RegistrationForm, LoginForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('blockchain.html')


@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         if form.email.data == 'rohit224455@gmail.com' and form.password.data == 'rohit@123':
             flash(f'Login successfully for {form.email.data}',category='success')
             return redirect(url_for('account'))
         else:
             flash(f'Login unsuccessfully for {form.email.data}',category='danger')
             return redirect(url_for('home'))

    return render_template('login.html',form=form)

@app.route("/register",methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}',category='success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)
 

 
