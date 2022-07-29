from abc import abstractmethod
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

    def display(self):
        pass

    def save(self):
        pass


class ShiftCipher(Algorithms):
        
    def encryption(self):
        pass

    def decryption(self):
        pass
    
class HillCipher(Algorithms):
    
    def encryption(self):
  
        k = 0
        for i in range(3):
            for j in range(3):
                keyMatrix[i][j] = ord(self.key[k]) % 65
                k += 1
        for i in range(3):
                messageVector[i][0] = ord(self.plain_text[i]) % 65
        for i in range(3):
            for j in range(1):
                cipherMatrix[i][j] = 0
                for x in range(3):
                    cipherMatrix[i][j] += (keyMatrix[i][x] *
                                           messageVector[x][j])
                cipherMatrix[i][j] = cipherMatrix[i][j] % 26
        CipherText = []
        for i in range(3):
            CipherText.append(chr(cipherMatrix[i][0] + 65))
        print("Ciphertext: ", "".join(CipherText))
        
class CaesarCipher(Algorithms):
    
    def encryption(self):
        result = ''
        for i in range(len(self.plain_text)):
            char = self.plain_text[i]
            if (char.isupper()):
                result += chr((ord(char) + self.key-65) % 26 + 65)
            else:
                result += chr((ord(char) + self.key - 97) % 26 + 97)
        self.cipher_text = result


 
