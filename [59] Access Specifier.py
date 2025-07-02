'''
class Employee:
    def __init__(self):
        self._name = "Yashvi"

a = Employee()
print(a._name)
'''
class Employee:
    def __init__(self):
        self.__name = "Yashvi"

a = Employee()
#print(a._name)
print(a._Employee__name)
print(a.__dir__())

