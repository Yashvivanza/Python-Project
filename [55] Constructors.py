# A constructor is a special method in a class used to create and initialize an object of a chain.
# Syntax :- def __init__(self):
''' class ABC:
     def ABC(self):
'''

class Person:

    def __init__(self, n, o):
        print("Hey I am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ} peron")


a = Person("Yashvi", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# to change name
#a.name = "Divya"
#a.occ = "HR"
#a.info()
