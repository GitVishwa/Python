#create a program that asks the user for a number and then prints out a list of all the divisors of that number

number = int(input("Enter the number : "))

divList = []

for num in range(1,number+1):
	if number % num is 0:
		divList.append(num)

print divList
