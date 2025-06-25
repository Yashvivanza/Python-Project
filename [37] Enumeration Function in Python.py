# Enumeration is a built in function , that can also be used in tuples, string
# In simple words :- at one time we will get two the thing its self and its index number.
marks = [12, 56, 32, 98, 12, 45, 1 ,4]

index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("Yashvi , awesome!")
    index +=1


print("  ")


# same code
marks = [12, 56, 32, 98, 12, 45, 1 ,4]

for index, mark in enumerate(marks , start=1):
    print(mark)
    if (index == 3):
        print("Yashvi , awesome!")
    index +=1

# start=1 indicates the  location where we can place Yashvi, awesome! ( i.e when we want to change start value )
