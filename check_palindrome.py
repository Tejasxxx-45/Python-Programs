# Program 3: Check if a string is palindrome
string = input("Enter a string: ")
if string == string[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")