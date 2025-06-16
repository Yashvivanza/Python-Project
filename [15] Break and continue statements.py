#Break Statements - leave the loop
for i in range(12):
    if(i==10):
        break
    print("5 X", i, "=", 5 * i)

print("")

#Continue Statements - leave the Iteration
for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i )