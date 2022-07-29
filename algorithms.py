#Importing all the necessary libraries
from abc import abstractmethod
from ast import Constant

'''For our software we need one class which is used to define all the algorithms
   The Algorithms class has 3 functions present in it.
   __init__ - Similar to constructors includes key, plaintext and ciphertext
   encryption - Function which consists of all the operations needed to encrypt the text in the file
   decryption - Function which consists of all the operations needed to decrypt the text in the file
   
'''

class Algorithms:

    def __init__(self, key):
        self.key = key
        self.plain_text = ''
        self.cipher_text = ''

    @abstractmethod
    def encryption(self):
        pass

    @abstractmethod
    def decryption(self):
        pass
    
  
#The child class RailFence inherith attributes from the main class and implements its encryption and decryption function
class RailFence(Algorithms):

    #Function to do the encryption process
    def encryption(self):
        text = self.plain_text
        key = self.key
        rail = [['\n' for i in range(len(text))] for j in range(key)]
     
    # to find the direction
        dir_down = False
        row, col = 0, 0
         
        for i in range(len(text)):
             
            # check the direction of flow
            # reverse the direction if we've just
            # filled the top or bottom rail
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
             
            # fill the corresponding alphabet
            rail[row][col] = text[i]
            col += 1
             
            # find the next row using
            # direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
        # now we can construct the cipher
        # using the rail matrix
        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        hc_desc = "1.In the rail fence cipher, the plain-text is written downwards and diagonally on successive rails of an imaginary fence. \n 2.When we reach the bottom rail, we traverse upwards moving diagonally, after reaching the top rail, the direction is changed again. Thus the alphabets of the message are written in a zig-zag manner. \n 3.After each alphabet has been written, the individual rows are combined to obtain the cipher-text.\n\n"
        self.cipher_text = hc_desc + "" . join(result)

    #Function to do the decryption process
    def decryption(self):
        text = self.cipher_text
        key = self.key
        rail = [['\n' for i in range(len(cipher))] for j in range(key)]
     
    # to find the direction
        dir_down = None
        row, col = 0, 0
         
        # mark the places with '*'
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
             
            # place the marker
            rail[row][col] = '*'
            col += 1
             
            # find the next row
            # using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
                 
        # now we can construct the
        # fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and
                   (index < len(cipher))):
                    rail[i][j] = cipher[index]

        result = []
        row, col = 0, 0
        for i in range(len(cipher)):
             
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key-1:
                dir_down = False
                 
            # place the marker
            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1

            if dir_down:
                    row += 1
            else:
                row -= 1
        hcDec = "1.Hence, rail matrix can be constructed accordingly. Once we’ve got the matrix we can figure-out the spots where texts should be placed (using the same way of moving diagonally up and down alternatively ).\n 2.Then, we fill the cipher-text row wise. After filling it, we traverse the matrix in zig-zag manner to obtain the original text.\n\n"
        self.plain_text = hcDec + "".join(result)
        
       
#The child class ShiftCipher inherith attributes from the main class and implements its encryption and decryption function
class ShiftCipher(Algorithms):
    
    #Function to do the encryption process
    def encryption(self):
        result = ''
        for i in range(len(self.plain_text)):
            #Takes in each individual character from the text and with the help of the key given as input and bases on the case of the alphabet, it is encrypted
            char = self.plain_text[i]
            if (char.isupper()):
                result += chr((ord(char) + self.key-65) % 26 + 65)
            else:
                result += chr((ord(char) + self.key - 97) % 26 + 97)
        Shiftalgo_enc = "1.Traverse the given text one character at a time \n 2.For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text \n 3.Return the new string generated. \n \n"
        self.cipher_text = Shiftalgo_enc + result


    #Function to do the decryption process
    def decryption(self):
        message = self.cipher_text #encrypted message
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for key in range(len(LETTERS)):
            translated = ''
            #Takes in each individual character from the text and checkes whether it is an alphabet and then decryptis it with the help of the key given in as the input
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
        Shiftalgo_dec = "create a function that will accomplish shifting in the opposite path to decrypt the original text. However, we can use the cyclic property of the cipher under the module. \n Cipher(n) = De-cipher(26-n) \n \n"
        self.plain_text = Shiftalgo_dec + translated
        

#The child class ShiftCipher inherith attributes from the main class and implements its encryption and decryption function
class VigenereCipher(Algorithms):

    
    ''' This function generates the
        key in a cyclic manner until
        it's length isn't equal to
        the length of original text
    '''
    def generateKey(string, key):
        key = list(key)
        if len(string) == len(key):
            return(key)
        else:
            for i in range(len(string) -
                        len(key)):
                key.append(key[i % len(key)])
        return("" . join(key))

    '''This function returns the
       encrypted text generated
       with the help of the key
    '''
    def encryption(self):

        key = VigenereCipher.generateKey(self.plain_text,self.key)

        cipher_text = []

        for i in range(len(self.plain_text)):
            x = (ord(self.plain_text[i]) +
                    ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        cipher_text = "".join(cipher_text)
        self.cipher_text = "Ei = (Pi + Ki) mod 26 \n \n "  + cipher_text


    '''This function decrypts the
       encrypted text and returns
       the original text
    '''
    def decryption(self):

        key = VigenereCipher.generateKey(self.cipher_text,self.key)
        
        orig_text = []
        for i in range(len(self.cipher_text)):
            x = (ord(self.cipher_text[i]) -
                ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        plain_text = "" . join(orig_text)
        self.plain_text = "Di = (Ei - Ki + 26) mod 26 \n \n" + plain_text
