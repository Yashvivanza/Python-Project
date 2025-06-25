a = input("Enter the number: ")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except:
    print("Sorry some error occurred")

print("Some lines of code")
print("End of program")

print(" ")

try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Numbered entered is not an integer")
except IndexError:
    print("Index Error")
