class Person:
    name = "Yashvi"
    occupation = "Software Developer"
    network = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Hiral"
a.occupation = "Software Engineer"
print(a.name)
print(a.occupation)
a.info()