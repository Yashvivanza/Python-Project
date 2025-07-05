# (Q.1) Explain arithmetic, relational and logical operators in Python with examples.

# ARITHMETIC OPERATOR
a = 2
b = 4
print("Addition : ",a + b )
print("Subtraction : ",a - b )
print("Multiplication : ",a * b )
print("Division : ",a / b )
print("Modulus : ",a % b )
print("Exponent : ",a ** b )
print("Floor Division : ",a // b )

print(" ")

# RELATIONAL OPERATOR
a = 3
b = 6
print("Greater than : ",a > b )
print("Less than : ",a < b )
print("Greather than or equal to : ",a >= b )
print("Less than or equal to : ",a <= b )
print("Not equal to : ",a != b )
print("Equal to : ",a == b )

print(" ")

# LOGICAL OPERATOR
x = 5
y = 10
z = 15
print((x > y) and (y > z))
print((x < y) or (y < z))
print(not (x > y))

print(" ")

# (Q.2) What are the variable naming conventions in Python? Explain with example.
# In Python, variable naming conventions are important for readability and maintainability of code.
# Python uses specific rules and best practices for naming variables to make code easier to understand.
# (1) Rules for naming
#     my_var = 10  , var_123 = 10 , myVar = 20,condition = 10
#     1st_var , var-123 = 10 , myvar = 20 ,if = 10 [invalid]
# (2) Best practices for naming variables
#     age = 25 , student_age = 20 , firsrt_name = "Yashvi"
#     a = 25 , studentAge = 20,firstname = "Yashvi"

student_name = "Yashvi"
age = 18
total_price = 105.75
MAX_HEIGHT = 157
is_valid = True
print("Student Name : ",student_name )
print("Age of Student : ",age )
print("Total Price : ",total_price )
print("Maximum height of Student : ",MAX_HEIGHT )
print("Is Valid : ",is_valid )
