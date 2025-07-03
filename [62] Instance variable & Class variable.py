class Employee:
    companyName = "Apple"
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in{self.companyName} is {self.raise_amount}")

emp1 = Employee("Yashvi")
emp1.showDetails()
emp1.raise_amount = 0.3
emp2 = Employee("Hiral")
emp2.showDetails()
Employee.showDetails(emp1)
Employee.showDetails(emp2)