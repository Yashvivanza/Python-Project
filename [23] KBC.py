<<<<<<< HEAD
#Create a program capable of displaying questions to the user like KBC.
#Use List data type to store the questions and their correct answers
#Displaying the final amount the person is taking home after playing the game.

questions =[
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0

i=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}  b. {question[2]} ")
    print(f"c. {question[3]}  d. {question[4]} ")
    reply = int(input("Enter your answer(1-4) :- "))
    if(reply == question[-1]):
        print(f"Correct Answer, you have won Rs. {levels[i]}")
        if( i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000

    else:
        print("Wrong Answer.")
=======
#Create a program capable of displaying questions to the user like KBC.
#Use List data type to store the questions and their correct answers
#Displaying the final amount the person is taking home after playing the game.

questions =[
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
["Which language was used to create facebook?","Python","French","JavaScript","Php","None",4],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0

i=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}  b. {question[2]} ")
    print(f"c. {question[3]}  d. {question[4]} ")
    reply = int(input("Enter your answer(1-4) :- "))
    if(reply == question[-1]):
        print(f"Correct Answer, you have won Rs. {levels[i]}")
        if( i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000

    else:
        print("Wrong Answer.")
>>>>>>> 78fc11a0f9ace23475a48b979aa5e60d6dbca8ed
        break