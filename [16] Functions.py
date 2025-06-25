"""
    A function is a block of code that performs a specific task whenever it is called.
    1. Built-in functions - These functions are defined and pre-coded in python. examples:- len(),sum(),type(),
                            range(), list(),set(),print(),etc.
    2.User-defined functions - We can create functions to perform specific task as per our needs.
                                def calculateGmean(a,b):
                                    mean = (a*b)/(a+b)
                                    print(mean)
"""
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLessThan(a,b):
    pass # pass means go to next step  and when you want it come back here.


a = 2
b = 6
#gmean1 = (a*b)/(a+b)
#print(gmean1)
isGreater(a,b)
calculateGmean(a,b)

c = 3
d = 2
#gmean2 = (c*d)/(c+d)
#print(gmean2)
isGreater(c,d)
calculateGmean(c,d)