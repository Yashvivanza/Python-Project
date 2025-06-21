#Recursion is basically a function, but it calls a function in same function is called recursion.
# FACTORIAL EXAMPLE
'''
    factorial(7) = 7*6*5*4*3*2*1
    factorial(6) = 6*5*4*3*2*1
    factorial(5) = 5*4*3*2*1
    factorial(4) = 4*3*2*1
    factorial(0) = 1
'''
# factorial(n) = n * factorial(n-1)
def factorial(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
# print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

print("")

#FIBONACCI SERIES EXAMPLE
def fibonacci(n):
    a, b = 0, 1
    for a in range(n):
        print(a,end=" ")
        a, b = b, a+b
fibonacci(5)
