from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY']='thisismyblockchain'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/dlt_transcation'


db=SQLAlchemy(app) #to initialize database file inside the sqlalchemy
bcrypt=Bcrypt(app)  # instantiate Bcrypt class in flask app
login_manager =LoginManager(app) 
from crcoin import routes