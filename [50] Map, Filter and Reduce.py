# MAP :- The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# Syntax :- map(function , iterate)
def cube(x):
    return x * x * x
print(cube(2))


l = {1,2,4,6,4,3}
newl = []
for item in l:
    newl.append(cube(item))
print(newl)
    #or
l = {1,2,4,6,4,3}
newl = list(map(cube, l))
        # or
newl = list(map(lambda x: x*x*x, l))
print(newl)


# Filter :- The filter function filters a sequence of elements based on a given predicate ( a function that returns a boolean value) and returns a new sequence containing only the elements that meet the prediction.
# Syntax :- filter (predicate , iterate)
def filter_function(a):
    return a>2
newnewl = list(filter(filter_function, l))
print(newnewl)


# Reduce :- The reduce function is a higher -order function that applies a function to as sequence and return single value. It is a part of the functools module in python .
# Syntax :- reduce(function, iterate)
from functools import reduce

numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)