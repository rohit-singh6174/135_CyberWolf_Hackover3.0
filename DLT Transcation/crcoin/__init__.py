from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from crcoin.blockchain import *

app = Flask(__name__)

app.config['SECRET_KEY']='thisismyblockchain'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/dlt_transcation'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app) #to initialize database file inside the sqlalchemy
bcrypt=Bcrypt(app)  # instantiate Bcrypt class in flask app
login_manager =LoginManager(app) 
blockchainObj = Blockchain();

from crcoin import routes