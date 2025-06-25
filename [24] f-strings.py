letter = "Hey my name is {} and I am form {}"
name = "Yashvi"
country = "India"
print(letter.format(name,country))

print("")

letter = "Hey my name is {1} and I am form {0}"
name = "Yashvi"
country = "India"
print(letter.format(country,name)) # or
print(f"Hey my name is {name} and I am from {country}")

print("")
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09999))

'''or'''
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print("")
print(f"{2 * 30}")
print(type(f"{2 * 30}"))