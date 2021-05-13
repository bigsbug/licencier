import os
import platform
import getpass
import uuid
import hashlib




class license:
    def __init__(self,______________,_________________):
        self.________________ = ______________
        self._________________ = str(_________________)
    def ___(self):
        __________________base = self._________________
        _________________ = getpass.getpass(str().join(map(chr,[69, 110, 116, 101, 114, 32, 121, 111, 117, 114, 32, 80, 97, 115, 115, 119, 111, 114, 100, 32, 58, 32])))
        if _________________ == __________________base:
            try:
                os.remove(self.________________)
            except:
                pass
            _____ =str(platform.processor()).encode(str().join(map(chr,[97, 115, 99, 105, 105])))
            ______ = "Created by @super1nova ".encode(str().join(map(chr,[97, 115, 99, 105, 105])))
            _______ = str(uuid.uuid4().hex).encode(str().join(map(chr,[97, 115, 99, 105, 105])))
            ________ = hashlib.pbkdf2_hmac(str().join(map(chr,[115, 104, 97, 53, 49, 50])),______+_____+_______,_______, (~~1001001))
            _________ = str(________.hex()).encode(str().join(map(chr,[97, 115, 99, 105, 105])))
            __________ =open(self.________________,str().join(map(chr,[119, 98])))
            __________.write(_________+_______)

        else:
            print(str().join(map(chr,[84, 104, 101, 32, 112, 97, 115, 115, 119, 111, 114, 100, 32, 105, 115, 32, 105, 110, 99, 111, 114, 114, 101, 99, 116, 46])))

    def ____(self):
        ___________ = open(self.________________,str().join(map(chr,[114]))).read()
        _____ =str(platform.processor()).encode(str().join(map(chr,[97, 115, 99, 105, 105])))
        ______ = "Created by @super1nova ".encode(str().join(map(chr,[97, 115, 99, 105, 105])))
        try:
            _______ =str( ___________[len(___________)-32:] ).encode(str().join(map(chr,[97, 115, 99, 105, 105])))
        except:
            print(str().join(map(chr,[84, 104, 101, 32, 75, 101, 121, 32, 105, 115, 32, 105, 110, 99, 111, 114, 114, 101, 99, 116, 44, 32, 80, 108, 101, 97, 115, 101, 32, 100, 101, 108, 101, 116, 101, 32, 102, 105, 108, 101, 32]))+self.________________+str().join(map(chr,[32, 97, 110, 100, 32, 116, 114, 121, 32, 97, 103, 97, 105, 110, 33])))
            return False
        ________ = hashlib.pbkdf2_hmac(str().join(map(chr,[115, 104, 97, 53, 49, 50])),______+_____+_______,_______, (~~1001001))
        _________ = str(________.hex()).encode(str().join(map(chr,[97, 115, 99, 105, 105])))
        _____________ = str(___________[:len(___________)-32]).encode(str().join(map(chr,[97, 115, 99, 105, 105])))
        if _____________ == _________:
            return True
        else:
            print(str().join(map(chr,[84, 104, 101, 32, 75, 101, 121, 32, 105, 115, 32, 105, 110, 99, 111, 114, 114, 101, 99, 116, 44, 32, 80, 108, 101, 97, 115, 101, 32, 100, 101, 108, 101, 116, 101, 32, 102, 105, 108, 101, 32]))+self.________________+str().join(map(chr,[32, 97, 110, 100, 32, 116, 114, 121, 32, 97, 103, 97, 105, 110, 33])))
            return False

    def check(self):
        if platform.os.path.isfile(self.________________):
            return self.____()     
        else:
            print(str().join(map(chr,[70, 105, 108, 101, 32]))+self.________________+str().join(map(chr,[32, 100, 111, 110, 39, 116, 32, 101, 120, 105, 115, 116])))
            self.___()

