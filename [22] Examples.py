<<<<<<< HEAD
import time
timestamp = time.strftime('%H : %M : %S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

print(" ")
import time
t = time.strftime('%H : %M : %S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
=======
import time
timestamp = time.strftime('%H : %M : %S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

print(" ")
import time
t = time.strftime('%H : %M : %S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
>>>>>>> 78fc11a0f9ace23475a48b979aa5e60d6dbca8ed
    print("Good Night Sir!")