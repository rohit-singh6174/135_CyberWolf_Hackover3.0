from blockchain import *
from time import time
import  pprint

pp = pprint.PrettyPrinter(indent=1)

blockchain =Blockchain();


transcation = Transaction("Rohit","Vrushabh",30)

blockchain.pendingTransactions.append(transcation)
blockchain.minePendingTransactions("checkit")

pp.pprint(blockchain.chainJSONencode())
print("Length :",len(blockchain.chain))

