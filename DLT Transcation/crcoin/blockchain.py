from flask import Flask
from Crypto.PublicKey import RSA
from time import time


class Blockchain(object):
    def generateKeys(self):#RSA key generation for users
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