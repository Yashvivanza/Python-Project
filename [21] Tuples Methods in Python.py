countries = ("Spain" , "Italy" , "India", "England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

#Maipulating Tuples
print("")
countries = ("Pakistan","Afghanistan","Bangladesh","ShriLanka")
counteries2 = ("Vietnam","India","China")
sounthEastAisa = countries + counteries2
print(sounthEastAisa)

#Tuple Methods
#1. count() method

print("  ")
Tuple1 = (0,1,2,3,2,3,1,3,2)
res = Tuple1.count(3)
print("Count of 3 in Tuple1 is: ",res)

#2. index() method :- returns thr first occurence of the given element from the tuple
Tuple1 = (0,1,2,3,2,3,1,3,2)
res = Tuple1.index(2)
print("Count of 2 in Tuple1 is: ",res)
Tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = Tuple1.index(3,4,8)
print("Count of 3 in Tuple1 is: ",res)
