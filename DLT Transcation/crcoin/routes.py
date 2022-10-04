#HACKOVER3.0
from flask import Flask, render_template, url_for, redirect, flash
from crcoin import app,db,bcrypt
from crcoin.forms import RegistrationForm, LoginForm
from crcoin.models import User
from flask_login import login_user,logout_user,current_user,login_required
from Crypto.PublicKey import RSA
from crcoin import blockchainObj

@app.route("/")
@app.route("/home")
def home():
    return render_template('blockchain.html')



@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/account")
@login_required
def account():
    return render_template('account.html')


@app.route("/register",methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    form=RegistrationForm()
    if form.validate_on_submit():
         u_email= User.query.filter_by(email=form.email.data).first()
         
         if u_email:
            u_username=User.query.filter_by(username=form.username.data).first()

            if u_username:
                 flash(f'Account already created for {form.username.data}',category='danger')
            else:
                 flash(f'Account already created for {form.email.data}',category='danger') 

         else:
            encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #genearte hash of 60 characters
            keyGen = blockchainObj.generateKeys()
            user= User(name=form.name.data,username=form.username.data,email=form.email.data,password=encrypted_password,key=keyGen)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created successfully for {form.username.data}',category='success')
            return redirect(url_for('home'))
    
    return render_template('register.html',form=form)

    
@app.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
         user= User.query.filter_by(email=form.email.data).first()
         if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash(f'Login successfully for {form.email.data}',category='success')
            return redirect(url_for('account'))
         else:
            flash(f'Login unsuccessfully for {form.email.data}',category='danger')
            return redirect(url_for('home'))

    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


 

 
