tup = (1,5, "green",True)

#tup[0] = 90 :- this is list where tuple cannot change and list can change
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-2])
print(tup[-1])

if 5 in tup:
    print("Yes 5 is present in this tuple")

tup2 = tup[1:4]
print(tup2)

