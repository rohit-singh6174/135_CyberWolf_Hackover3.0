from crcoin import db,login_manager  # it will look from _init_ file by default in that it will look for db variable if it there it will import   
from datetime import datetime
from flask_login import UserMixin
from flask import url_for, redirect

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('register'))

class User(db.Model,UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(40),unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    key = db.Column(db.String(100000),unique=True,nullable=False)

    def __repr__(self):
        return f'\n name: {self.name},\n username: {self.username},\n email: {self.email},\n password: {self.password},\ndate: {self.date_created.strftime("%d/%m/%Y, %H:%M:%S")}, \nkey :{self.key}\n'
