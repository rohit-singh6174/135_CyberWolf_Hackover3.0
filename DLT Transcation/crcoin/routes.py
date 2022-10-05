#HACKOVER3.0
from flask import Flask, render_template, url_for, redirect, flash,jsonify, request
from crcoin import app,db,bcrypt
from crcoin.forms import RegistrationForm, LoginForm, TransactionForm
from crcoin.models import User
from flask_login import login_user,logout_user,current_user,login_required
from Crypto.PublicKey import RSA
from crcoin import blockchainObj
import pprint 

@app.route("/")
@app.route("/home")
def home():
    pp = pprint.PrettyPrinter(indent=4);
    blockchainObj.resolveConflicts();
    pp.pprint(blockchainObj.chainJSONencode());
    return render_template('blockchain.html', title = "Blockchain", blockchain = blockchainObj)


@app.route("/minerPage")
def minerpage():
    return render_template('minerPage.html', title = "Mine", blockchain = blockchainObj)
    

@app.route("/account")
@login_required
def account():
    return render_template('account.html',blockchain = blockchainObj)


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


@app.route("/transcation",methods=['POST', 'GET'])
@login_required
def transcation():
    print("Hello")
    form = TransactionForm()
    if form.validate_on_submit():
        print("Validation Successful")
        receiver =User.query.filter_by(username=form.receiver.data).first()
        if receiver:
            sendingamt=form.amount.data
            if sendingamt <= blockchainObj.getBalance(form.sender.data):
                    feedback = blockchainObj.addTransaction(form.sender.data, form.receiver.data, form.amount.data, form.key.data, form.key.data); 
                    if feedback:
                        flash(f'Transaction Successfull',category='success')
                    else:
                        flash(f'Transaction unsuccesfull',category='danger')
                    
            else:
                flash(f'Insufficient funds',category='danger')
        else:
            print("Invalid Receiver")
            flash(f'Invalid Receiver',category='danger')    
    
    return render_template('transcation.html', title = "Transaction",blockchain = blockchainObj,form=form)


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json();
    required = ['sender', 'reciever', 'amt']
    if not all(k in values for k in required):
        return 'Missing values', 400;

    index = blockchainObj.addTransaction(values['sender'], values['reciever'], values['amt'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201;




@app.route('/mine', methods=['GET'])
def mine():
    print("madeit");
    miner = request.args.get('miner', None);
    lastBlock = blockchainObj.getLastBlock();

    if len(blockchainObj.pendingTransactions) <= 1:
        flash(f'Not enough pending transactions to mine! (Must be > 1)',category='danger');
    else:        
        feedback = blockchainObj.minePendingTransactions(miner);
        if feedback:
            flash(f'Block Mined! Your mining reward has now been added to the pending transactions!', category='success');

        else:
            flash(f'Error!',category='danger');

    return render_template('minerPage.html', title = "Mine", blockchain = blockchainObj);
