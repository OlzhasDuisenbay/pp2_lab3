"""Define a class which has atleast two methods:
getString: to get a string from console input printString:to print the string in upper case."""
class StringProcessor:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())
obj = StringManipulator()
obj.getString()
obj.printString()
#kbtu >>> KBTU
