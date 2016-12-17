#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num = int(input("Enter the number : "))

res = num % 2

if res is 0:
	print("THE NUMBER IS EVEN")
else:
	print("THE NUMBER IS ODD")


