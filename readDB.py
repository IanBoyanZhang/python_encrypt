import getpass
import sys
import os
import pickle
from AEScryp import AEScryp
from myColor import setColor

if __name__ == '__main__':
    privateKey = getpass.getpass('private key:')
    temp_cryptor = AEScryp(privateKey)
    f = open('accounts.db', 'rb')
    data = pickle.load(f)
    for cur in data:
        accountName = temp_cryptor.decrypt(cur)
        user_pass = temp_cryptor.decrypt(data[cur]).split('&')
        username, password = user_pass[0], user_pass[1]
        print setColor('green',accountName) + ' ' + setColor('blue',username) + ' ' + setColor('yellow', password)
    f.close()
