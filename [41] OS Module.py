# The os module  in python is a built-in library that provides functions for interacting with the operating system.
# It allows us to perform a wide variety of tasks, such as reading and writing files , interacting with the file system, and running system commands.
# We can read , rename ,  we want to know how many day/ tutorial are present
'''import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day{i + 1}")
'''

# If we want to change from folder data :- like Day 1, 2, to 100 and change to Tutorial 1,2 to 100 then,
'''import os
for i in range(0,100):
    os.rename(f"data/Day{i + 1}" , f"data/Tutorial{i + 1}")
'''

'''
import os
for i in range(0,100):
    os.rename(f"data/Tutorial{i + 1}" , f"data/Tutorial {i + 1}")
'''
