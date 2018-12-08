'''
Description:
    Implementation of Route cipher for assignment.

Author:
    Jiaqi Zhang
    
Date:
    2018-12-8
'''
import math
import re

class Encoder:

    def __init__(self):
        self.plainText=""
        self.encodedText=""
        self.colNum=1

    def ciphering(self,rowNum,colNum,plainText=""):
        # Check input invalidation
        if rowNum*colNum<len(plainText):
            print("The size of grid should be larger than the length of your text.")
        if plainText == "":
            print("Your plain text should contain at least one character !")
            return None
        if re.match(r'[A-Za-z]*', plainText).group() == "" :
            print("Your plain text should contain only english alphabets !")
            return None
        plainText = plainText.lower()
        # Ciphering
        textPart=[]
        for i in range(rowNum):
            if len(plainText)>=colNum:
                textPart.append(plainText[:colNum])
                plainText=plainText[colNum:]
            else:
                plainText=plainText.ljust(colNum,"%")
                textPart.append(plainText[:colNum])
        encodedText = ""
        for j in range(colNum):
            for i in range(rowNum):
                encodedText+=textPart[i][j]
        return encodedText

    def deciphering(self, rowNum,colNum,encodedText=""):
        # Check input invalidation
        if encodedText == "":
            print("Your plain text should contain at least one character !")
            return None
        if re.match(r'[A-Za-z]*(%)*[A-Za-z]*', encodedText).group() == "" :
            print("Your encoded text should contain only english alphabets !")
            return None
        encodedText = encodedText.lower()
        # Deciphering
        textPart = []
        for i in range(rowNum):
            textPart.append(encodedText[:colNum])
            if len(encodedText) >= colNum:
                encodedText = encodedText[colNum:]
            else:
                encodedText = encodedText.rjust(colNum, "%")
        plainText = ""
        for j in range(colNum):
            for i in range(rowNum):
                plainText += textPart[i][j]
        return plainText.strip("%")


def mainMenu():
    encoder = Encoder()
    print("=========== MENU ============")
    while True:
        choice = input("What do you want ?\n1. Ciphering\n2. Deciphering\n3. Exit\n")
        if choice != "1" and choice != "2" and choice != "3":
            print("You must enter 1, 2 or 3 !\n")
            continue
        elif choice=="1":
            plainText = input("Enter your plain text:")
            rowNum = input("Enter number of rows:")
            colNum = input("Enter number of columns:")
            encodedText = encoder.ciphering(int(rowNum),int(colNum),plainText)
            if encodedText!=None:
                print("Encoded text is :", encodedText)
        elif choice == "2":
            encodedText = input("Enter your encoded text:")
            rowNum = input("Enter number of rows:")
            colNum = input("Enter number of columns:")
            plainText = encoder.deciphering(int(rowNum), int(colNum), encodedText)
            if encodedText!=None:
                print("Plain text is :", plainText)
        else:
            break
        print("----------------------------")
    print("===========================")


if __name__ == '__main__':
    mainMenu()