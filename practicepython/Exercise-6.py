#Ask the user for a string and print out whether this string is a palindrome or not

string = str(input("Enter the string : "))

word = string[::-1]

if word == string:
	print("The string is palindrome: ")
else:
	print("The string is not palindrome: ")

