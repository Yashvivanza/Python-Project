# union() and update()
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2) # it means we have to put s2 value which is not in present in s1 that is 3 and 7
print(s1,s2)
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
cities3 = cities1.union(cities2)
print(cities3)

print(" ")

# Intersection and intersection_update()
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
cities3 = cities1.intersection(cities2)
print(cities3)
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
cities1.intersection_update(cities2)
print(cities1)

print(" ")

# Symmetric_difference and symmetric_difference_update()
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
cities1.symmetric_difference_update(cities2)
print(cities1)

# Set Methods
print("\n\nSET METHODS ")

#1. isdisjoint() - same then false if no intersection then true
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
print(cities1.isdisjoint(cities2))

print(" ")

#2. issuperset()
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Seoul" , "Kabul"}
print(cities1.issuperset(cities2))
cities3 ={"Seoul" , "Madrid" , "Kabul"}
print(cities1.issuperset(cities3))

print(" ")

#3. issubset()
cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Seoul" , "Kabul"}
print(cities1.issuperset(cities2))
cities3 ={"Tokyo" , "Madrid" , "Delhi"}
print(cities1.issuperset(cities3))
print(cities3.issubset(cities1))

print(" ")

#4. add()
cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities.add("Helsinki")
print(cities)

print(" ")

#5. update()
cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities1 = {"Helsinki", "Belgim"}
cities.update(cities1)
print(cities)

print(" ")

#6. remove() / discard()
cities = {"Tokyo" ,"Helsinki", "Madrid" , "Berlin" , "Delhi"}
cities.remove("Helsinki")
print(cities)

print(" ")

#7. pop()
cities = {"Tokyo" ,"Helsinki", "Madrid" , "Berlin" , "Delhi"}
item = cities.pop()
print(cities)
print(item)

print(" ")

#8.del
cities = {"Tokyo" ,"Helsinki", "Madrid" , "Berlin" , "Delhi"}
del cities # here del means it completely deletes the cities
print(cities)
