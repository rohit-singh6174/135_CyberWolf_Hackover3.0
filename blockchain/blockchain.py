import hashlib
import json
from textwrap import dedent
from uuid import uuid4
import jsonpickle
from flask import Flask
from urllib.parse import urlparse
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from time import time
from datetime import datetime
import requests

class Blockchain(object):
    def __init__(self):
        self.pendingTransactions = [];

    def generateKeys(self):#
        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open("private.pem", "wb")
        file_out.write(private_key)

        public_key = key.publickey().export_key()
        file_out = open("receiver.pem", "wb")
        file_out.write(public_key)
		
        print(public_key.decode('ASCII'));
        print(private_key.decode('ASCII'));
        return key.publickey().export_key().decode('ASCII');

    def addTransaction(self, sender, reciever, amt, keyString, senderKey):
        keyByte = keyString.encode("ASCII");
        senderKeyByte = senderKey.encode("ASCII");

        #print(type(keyByte), keyByte);

        key = RSA.import_key(keyByte);
        senderKey = RSA.import_key(senderKeyByte);

        if not sender or not reciever or not amt:
            print("transaction error ");
            return False;

        transaction = Transaction(sender, reciever, amt);

        transaction.signTransaction(key, senderKey);

        if not transaction.isValidTransaction():
            print("transaction invalid");
            return False;
        self.pendingTransactions.append(transaction);
        return len(self.chain) + 1;


  