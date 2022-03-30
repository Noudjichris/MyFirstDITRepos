from cgi import print_form
from msilib.schema import Class


class Human():
    def parler(self):
        print("Human can speak")
h1 = Human()
h1.parler()