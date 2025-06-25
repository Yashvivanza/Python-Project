a = int(input("Enter your age: "))
print("Your age is: ",a)

print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)
print("")
if(a>18):
    print("You can drive")
else:
    print("You can not drive")


#Example 2
print("")
num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negative. ")
elif (num == 0):
    print("Number is Zero.")
elif (num == 999):
    print("Number is special. ")
else:
    print("Number is positive. ")

print("I am happy.")