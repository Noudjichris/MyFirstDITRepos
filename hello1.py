from cgi import print_form
from msilib.schema import Class


class Human():
    def parler(self):
        print("Human can speak")

    def marcher(self):
        print("Human can walk")
h1 = Human()
h1.parler()