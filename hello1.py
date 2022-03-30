from cgi import print_form
from msilib.schema import Class


class Human():
    def parler(self):
        print("Human can speak")

    def marcher(self):
        print("Human can walk")
    def respirer(self):
        print("Human can breath")
h1 = Human()
h1.parler()
h1.marcher()
h1.respirer()