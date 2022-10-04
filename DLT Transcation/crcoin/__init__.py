from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY']='thisismyblockchain'
from crcoin import routes