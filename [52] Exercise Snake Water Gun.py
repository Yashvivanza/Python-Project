# SNAKE WATER GUN
'''
    Snake, Water and Gun is a variation os the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake , the water beats the gun , and the snake beats the water.
    Write a Python program to create a Snake Water GUn game in Python using if - else statements. Do not create any fancy GUI. use proper functions to check for win.
'''
print("Welcome to Snake - Water - Gun Game!")
print("Choose")
print("1. Snake")
print("2. Water")
print("3. Gun")

person = int(input("Enter your choice (1/2/3) : "))
computer = int(input("Enter computer's choice (1/2/3) : "))

options = {1: "Snake",2: "Water",3: "Gun"}
print(f"\nMy choice: {options.get(person,'Invalid')}")
print(f"Computer choice: {options.get(computer,'Invalid')}")

if person == computer:
    print("Its's a Tie!")
elif (person == 1 and computer == 2 ) or \
     (person == 2 and computer == 3) or \
     (person == 3 and computer ==1):
    print("You Win!")
elif (person == 2 and computer == 1) or \
     (person == 3 and computer == 2) or \
     (person == 1 and computer == 3):
    print("Computer Wins! 💻")
else:
    print("Invalid Input!")