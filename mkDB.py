#version 1.0
import getpass
import sys
import os
import pickle
from AEScryp import AEScryp

# mkDB [masfterfile]

def test(): #test code
    f = open('accounts.db', 'rb')
    data = pickle.load(f)
    for a in data:
        print 'usr name: '+a+' pas word: '+data[a]
        print 'new usr name: '+temp_cryptor.decrypt(a)+' new pas word: '+temp_cryptor.decrypt(data[a])
    f.close()
    return

if __name__ == '__main__':

    if len(sys.argv)<2 or len(sys.argv)>2:
        print 'Command Format: mkDB.py [file name for accounts]\noutput file will be accounts.db'
        exit()
    else:
        masterFile = sys.argv[1]
        # masterFile = getpass.getpass('file name: ')
        if not os.path.isfile(masterFile):
            print 'file not exist'
            exit()
        else:
            priKey = getpass.getpass('private key: ')
            temp_cryptor = AEScryp(priKey)
            data = {}
            accountdata = open(masterFile, 'rb')
            for line in accountdata:
                splited = line.split(',')
                key_encode = temp_cryptor.encrypt(splited[0])
                usrNpassData_encode = temp_cryptor.encrypt(splited[1]+'&'+splited[2].rstrip('\n'))
                data.update({key_encode:usrNpassData_encode})
            accountdata.close()
            f = open('accounts.db','wb')
            pickle.dump(data, f)
            f.close()
    #test()
