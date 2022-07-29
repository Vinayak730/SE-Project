#from UI import *
#from Encryption_Algorithms import *


class User:

    def __init__(self):
        self.option = None
        self.algo = None
        self.text = None
        self.key = None
        self.path = None

    def get_text(self):
        print(self.text) 
    '''
    def encrypt_or_decrypt(self):
        
        if self.algo == "shift_cipher":
            
            if self.option == "encrypt":
                obj = shift_cipher(self.key,self.text,None)
                obj.encrypt()
            else:
                obj = shift_cipher(self.key,None,self.text)
                obj.decrypt()
                
        if self.algo == "hillcypher":
            
            if self.option == "encrypt":
                obj = hillcypher(self.key,self.text,None)
                obj.encrypt()
            else:
                obj = hillcypher(self.key,None,self.text)
                obj.decrypt()

        if self.algo == "caesarcipher":
            
            if self.option == "encrypt":
                obj = caesarcipher(self.key,self.text,None)
                obj.encrypt()
            else:
                obj = caesarcipher(self.key,None,self.text)
                obj.decrypt()

        obj.display()
        obj.save()

    def view_file(self):
        
        if self.option == 'view':
            view_obj = View(path)
            view_obj.getTheFile()
'''






