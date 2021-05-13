import os
import platform
import getpass

try:
    import uuid
except:
    print('Please install the module uuid')
    os._exit(1)
try:
    import hashlib
except:
    print('Please install the module hashlib')
    os._exit(1)

# try:
#     from getmac import get_mac_address as MAC
# except:
#     print('Please install the module getmac')
#     os._exit(1)

class license:
    def __init__(self,NameFile,Password):
        self.FileName = NameFile
        self.Password = str(Password)
    def Active(self):
        password_base = self.Password
        password = getpass.getpass('Enter your password : ')
        if password == password_base:
            try:
                os.remove(self.FileName)
            except:
                pass
            # mac = str(MAC()).encode('ascii')
            cpu_name =str(platform.processor()).encode('ascii')
            licenses = "Created by @super1nova ".encode('ascii')
            uuids = str(uuid.uuid4().hex).encode('ascii')
            # key = hashlib.pbkdf2_hmac('sha512',mac+licenses+cpu_name+uuids,uuids, 100000)
            key = hashlib.pbkdf2_hmac('sha512',licenses+cpu_name+uuids,uuids, 100000)
            hash = str(key.hex()).encode('ascii')
            file_ =open(self.FileName,"wb")
            file_.write(hash+uuids)

        else:
            print('The password is incorrect.')

    def Verify(self):
        licen = open(self.FileName,'r').read()
        # mac = str(MAC()).encode('ascii')
        cpu_name =str(platform.processor()).encode('ascii')
        licenses = "Created by @super1nova ".encode('ascii')
        try:
            uuids =str( licen[len(licen)-32:] ).encode('ascii')
        except:
            print(f'The Key is incorrect, Please delete file "{self.FileName}" and try again!')
            return False
        # key = hashlib.pbkdf2_hmac('sha512',mac+licenses+cpu_name+uuids,uuids, 100000)
        key = hashlib.pbkdf2_hmac('sha512',licenses+cpu_name+uuids,uuids, 100000)
        hash = str(key.hex()).encode('ascii')
        result = str(licen[:len(licen)-32]).encode('ascii')
        if result == hash:
            return True
        else:
            print(f'The Key is incorrect, Please delete file "{self.FileName}" and try again!')
            return False

    def check(self):
        if platform.os.path.isfile(self.FileName):
            return self.Verify()     
        else:
            print(f'File "{self.FileName}" don\'t exist')
            self.Active()

if '__main__' in __name__:
    print('''
    For use this lib you need to import it in your code like this 

    import license 
    status = license('FileName','Password').check()

    the "status" can be True or False 

    ''')