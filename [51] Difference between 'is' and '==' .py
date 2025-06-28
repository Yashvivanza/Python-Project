# 'is' compares exact location of object in memory.OR compares the Identity of two objects
# '==' compares the values.

a = 4
b = "4"
print(a is b) # exact location of object in memory
print(a == b) # value

print(" ")

a = [1, 2, 3] # list
b = [1, 2, 3]
print(a is b)
print(a == b)

print(" ")

a = 3 # value and constant , cannot be change
b = 3
print(a is b)
print(a == b)

print(" ")


a = "Yashvi"
b = "Yashvi"
print(a is b)
print(a == b)

print(" ")


a = (1,2) # Tuple :- immutable
b = (1,2)
print(a is b)
print(a == b)

print(" ")


a = None
b = None
print(a is b)
print( a is None)
print(a == b)

print(" ")


a = None
b = [1, 2, 3]
print(a is b)
print( a is None)
print(a == b)
