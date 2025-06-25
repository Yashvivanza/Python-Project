#Iterating over a string
name = ("YASHVI")
for i in name:
    print(i) # or print(i)
    if(i=="A"):
        print("This is something special")

print("")

#Iterating over a list
colors = ["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

print("")

#range() - in range step method means (1,12,3) so it skips 3-3 numbers like 1, 4,7,10
for k in range(5):
    print(k,end=" ") # or print(k+1)
print("")
for k in range(1,9):
    print(k,end=" ")
print("")
for k in range(1,201):
    print(k)