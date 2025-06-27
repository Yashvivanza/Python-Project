
# The seek() and tell() functions are used to work with the objects and their positions within a file.
'''
    The seek() function allows us to move the current position within a file to a specific point. The Position is speccifies in bytes , and we can move other forward or backward from the current position.
'''

with open('file.txt', 'r') as f:
    print(type(f))

     # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)


'''
    The tell() function returns the current position within the file, in bytes.
'''

with open('file.txt', 'r') as f:
    # read the first 10 bytes
    data = f.read(5)

    # save the current position
    current_position = f.tell()

    # Seek to the saved positions
    f.seek(current_position)

'''
    The truncate() function :- When we open a file in python using the open functions, we can specify the mode in which we want to open the file.
'''
with open('sample.txt', 'w') as f:
    f.write("Hello World3!")
    #f.truncate(5)

    with open('sample.txt', 'r') as f:
        print(f.read())