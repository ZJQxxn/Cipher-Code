'''
Description:
    Implementation of Vigenere cipher for assignment.

Author:
    Jiaqi Zhang
    
Date:
    2018-12-8
'''
import math
import re

class Encoder:

    def ciphering(self,plainText="",key=""):
        # Check input invalidation
        if plainText=="":
            print("Your plain text should contain at least one character !")
            return None
        if re.match(r'[A-Za-z]*',plainText).group()=="" or " " in plainText:
            print("Your plain text should contain only english alphabets without any space!")
            return None
        if key=="":
            print("Your key text should contain at least one character !")
            return None
        if re.match(r'[A-Za-z]*', key).group() == "" or " " in key:
            print("Your key should contain only english alphabets without any space!")
            return None
        # Some initialization
        plainText=plainText.lower().replace(" ","")
        key=key.lower().replace(" ","")
        while len(key)<len(plainText):
            key+=key
        key=key[:len(plainText)]
        # Ciphering
        length=len(plainText)
        encodedText=""
        for i in range(length):
            tmp=(ord(plainText[i])+ord(key[i])-2*ord('a'))%26+ord("a")
            encodedText+=chr(tmp)
        return encodedText

    def deciphering(self,encodedText="",key=""):
        #Check input invalidation
        if encodedText == "":
            print("Your plain text should contain at least one character !")
            return None
        if re.match(r'[A-Za-z]*', encodedText).group() == "" or " " in encodedText:
            print("Your encoded text should contain only english alphabets without any space!")
            return None
        if key == "":
            print("Your key text should contain at least one character !")
            return None
        if re.match(r'[A-Za-z]*', key).group() == "" or " " in key:
            print("Your key should contain only english alphabets without any space!")
            return None
        # Some initialization
        encodedText = encodedText.lower().replace(" ", "")
        key = key.lower().replace(" ", "")
        while len(key) < len(encodedText):
            key += key
        key = key[:len(encodedText)]
        # Deciphering
        length = len(encodedText)
        plainText = ""
        for i in range(length):
            tmp = (ord(encodedText[i]) - ord(key[i])) % 26 + ord("a")
            plainText += chr(tmp)
        return plainText


def mainMenu():
    encoder = Encoder()
    print("=========== MENU ============")
    while True:
        choice = input("What do you want ?\n1. Ciphering\n2. Deciphering\n3. Exit\n")
        if choice != "1" and choice != "2" and choice != "3":
            print("You must enter 1 or 2 !\n")
            continue
        elif choice=="1":
            plainText = input("Enter your plain text:")
            key = input("Enter your key:")
            encodedText = encoder.ciphering(plainText, key)
            if encodedText!=None:
                print("Encoded text is :", encodedText)
        elif choice == "2":
            encodedText = input("Enter your encoded text:")
            key = input("Enter your key:")
            plainText = encoder.deciphering(encodedText, key)
            if encodedText!=None:
                print("Plain text is :", plainText)
        else:
            break
        print("----------------------------")
    print("===========================")


if __name__ == '__main__':
    mainMenu()