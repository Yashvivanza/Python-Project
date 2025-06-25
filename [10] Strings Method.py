# Strings are immutable
a = "Yashvi !!!!!!!!! Yashvi!!!! !!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())


#rstrip() method - removes any trailing characters
print("")
print(a.rstrip("!"))


#replace() method
print("")
print(a.replace("Yashvi","Riya"))


#split method
print("")
print(a.split(" "))


#Capitalize()
print("")
blogHeading = "introduction to python"
print(blogHeading.capitalize())


#center method()
print("")
str1 = "Welcome to Python"
print(str1.center(50))


#length and center
print("")
str2 = "Welcome to Python"
print(len(str2))
print(len(str2.center(50)))


#count() method
print("")
print(a.count("Yashvi"))


#swapcase()
print("")
str3 = "welcome to python!!!!"
print(str3.swapcase())


#find method()
print("")
str4 = "He's name is Dan. he is an Honest man."
print(str4.find("is"))


#index method()
"""print("")
str5 = "He's name is Dan. he is an Honest man."
print(str5.index("to"))""" #Value Error


#isalnum() :- A-Z , a-z , includes number
print("")
str6 = "WelcomeToThePython"
print(str6.isalnum())


#isalpha() :- A-Z , a-z , no numbers are involved
print("")
str7 = "Welcome00"
print(str7.isalpha())


#islower()
print("")
str8 = "welcome to the python"
print(str8.islower())


#isupper()
print("")
str9 = "WELCOME TO THE PYHTON"
print(str9.islower())


#isprintable()
print("")
str10 = "We wish you a Merry Christmas"
print(str10)
print(str10.isprintable())


#isspace() :- using spacebar tab button only
print("")
str11 = "       "#using tab
print(str11.isspace())
str11 = "          "#using spacebar
print(str11.isspace())


#istitle() :- Returns True only if the first letter of each word is capitalalized , else it returns false
print("")
str12 = "Welcome To Python"
print(str12.istitle())
str12 = "Welcome to Python"
print(str12.istitle())


#startswith()
print("")
str13 = "Welcome to Python!!!!"
print(str13.endswith("!!!!"))
str13 = "Welcome to Python!!!!"
print(str13.startswith("Welcome"))


#endswith()
print("")
str14 = "Welcome to Python!!!!"
print(str14.endswith("!!!!"))
str14 = "Welcome to Python!!!!"
print(str14.endswith("to",4,10))


#title()
print("")
str15 = "His nam eis Dan. Dan is an honest man."
print(str15.title())


