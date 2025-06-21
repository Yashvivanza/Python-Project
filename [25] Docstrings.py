#Docstrings:- they appear right after the defination of a functiona, methods, class or methods.

def square(n):
    ''' Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) # they display the comment, the doc string comment is written right below the function name or right above the function body

