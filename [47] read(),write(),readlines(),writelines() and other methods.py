""" READLINES() METHOD"""

f = open('myfile.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in maths is : {m1*2}")
    print(f"Marks of student {i} in english is : {m2*2}")
    print(f"Marks of student {i} in SST is : {m3*2}")

    print(line)

""" WRITELINES() METHOD"""
f = open('myfile.txt', 'w')
lines = {'line 1\n', 'line 2\n', 'line 3\n'}
f.writelines(lines)
f.close()


# writelines() method does not add new line characters between strings and the sequence.
