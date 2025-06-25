"""
Function Arguments:- Default Arguments
                     Keyword Arguments
                     Variable Arguments
                     Required Arguments
"""
from xml.dom.minidom import ProcessingInstruction

#(1)
print("DEFAULT ARGUMENTS:--")
def average(a,b):  # here a and b is required argument
    print("The average is ",(a+b)/2)
average(4,6)



def average(a=9 ,b=1):  # here a and b is default argument
    print("The average is ",(a+b)/2)
#average(4,6)
average()



def average(a=9 ,b=1):  # here a and b is default argument
    print("The average is ",(a+b)/2)
#average(4,6)
average(1,5) # here it uses 1 and 5 not 9 and 1



def average(a=9 ,b=1):  # here a and b is default argument
    print("The average is ",(a+b)/2)
#average(4,6)
average()



def average(a=9 ,b=1):
    print("The average is ",(a+b)/2)
#average(4,6)
average(5) # if i want b=1 as default  also it gives correct answer



def average(a=9 ,b=1):
    print("The average is ",(a+b)/2)
#average(4,6)
average(b=9) # if i want a=9 as default  also it gives correct answer



def name(fname,mname="John",lname ="Whatson"):
    print("Hello",fname,mname,lname)
name("Ajay")



def name(fname,mname,lname ="Whatson"):
    print("Hello",fname,mname,lname)
name("Ajay","Agrawal")



def name(fname,mname,lname):
    print("Hello",fname,mname,lname)
name("Ajay","Agrawal","Jain")


#(2)
print("  ")
print("KEYWORD ARGUMENTS:--")
def average(b=1,a=9):
    print("The average is ",(a+b)/2)
average()


#(3)
print("")
print("VARIABLE ARGUMENTS:--")
def average(*numbers):
    print(type(numbers))  # This will show <class 'tuple'>
    total = 0
    for i in numbers:
        total = total + i
    print("Average is", total / len(numbers))
#Call the function
average(10,10,10)

def average(*numbers):
    print(type(numbers))  # This will show <class 'tuple'>
    total = 0
    for i in numbers:
        total = total + i
    return total / len(numbers)
#Call the function
c = average(10,10,10)
print("Average is", c )


print("")
def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["mname"], name["lname"])
name(mname = "John",fname = "James", lname = "Smith")

#(4)
"""print("  ")
print("REQUIRED ARGUMENTS:--")  # here fname i.e a is compulsory to write(mention)
def name(fname, mname, lname="Raj"):
    print("Hello",fname,mname,lname)
name("Ajay","Rahul")"""
