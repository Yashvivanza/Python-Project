''' READING A FILE'''
f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# If we do f = open('myfile.txt') then also it runs because r is default
# If we do f = open('myfile1.txt' , 'w') then it creates myfile1.txt file

'''
 Modes in file
 1. read(r)
 2. write(w)
 3. append(a)
 4. create(x)
 5. txt(t) - rt
 6. binary(b) - rb
'''

''' WRITING A FILE'''
#f = open('myfile.txt', 'w')
#f.write('Hello,world')
#f.close()

''' THE "with" STATEMENT '''
with open('myfile.txt', 'a') as f:
    f.write('\nHey I am  inside with ')
