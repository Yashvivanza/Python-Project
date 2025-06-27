# A Lambda function is a small anonymous function without a name . It is denoted using the lambda keyword and has the following syntax:-
#   lambda argumenta: expression
def double(x):
    return x * 2

print(double(5))

# or
double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x,y,z: (x + y + z)/ 3
print(double(5))
print(cube(5))
print(avg(3,5, 10))


print(" ")

def appl(fx, value):
    return 6 + fx(value)

cube = lambda x: x * x * x


print(appl(lambda x: x * x * x,2))
        #or
print(appl(cube,2))