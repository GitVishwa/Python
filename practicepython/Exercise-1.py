#The program asks the name and age from user and tells them on which year they become 100 years old
#comiple it with python3

import datetime

get = datetime.datetime.now()

name = str(input("Enter your name: "))

age = int(input("Enter your age: "))

currentYear = get.year

century = ((100-age)+currentYear)

print("Your name is",name,"And your age is",age,"You will be 100 years old in",century)
