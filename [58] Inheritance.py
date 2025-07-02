class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"THe name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("THe default language is Python")
e1 = Employee("Rohan Das", 400)
e2 = Programmer("Yashvi", 4100)
e1.showDetails()
e2.showLanguage()