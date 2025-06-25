<<<<<<< HEAD
try:
    l = [1,5,6,7]
    i = int(input("Enter the index :- "))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am always exceuted")


# Difference between directly printing or use of finally keyword, gives same output.
# So using function we will see

print("  ")

def funct1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index :- "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always exceuted")
    #print("I am always exceuted")

x = funct1()
print(x)
=======
try:
    l = [1,5,6,7]
    i = int(input("Enter the index :- "))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am always exceuted")


# Difference between directly printing or use of finally keyword, gives same output.
# So using function we will see

print("  ")

def funct1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index :- "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always exceuted")
    #print("I am always exceuted")

x = funct1()
print(x)
>>>>>>> 78fc11a0f9ace23475a48b979aa5e60d6dbca8ed
