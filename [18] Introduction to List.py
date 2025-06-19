# List are ordered collection of data items
marks = [3,5,6,"Yashvi",True,2,4,8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print("")
print(marks[-3]) # Negative Index
print(marks[len(marks)-3]) # Positive Index
print(marks[5-3])
print(marks[2])

print("")
#Identify if the 7 is present  or not
if 7 in marks:
    print("Yes")
else:
    print("No")
if "Yashvi" in marks:
    print("Yes")
else:
    print("No")
if "ash" in "Yashvi":
    print("Yes")
else:
    print("No")


print("")
print(marks)
print(marks[1:-1])
print(marks[1:7])
print(marks[1:7:3]) # here 3 means it cuts 2 numbers from a list

#List Comprehension -  They are used for creating new lists from other iteration like tuples , lists.
print("")
lst =[ i*i for i in range(10)]
print(lst)
lst =[ i*i for i in range(10) if i%2==0]
print(lst)