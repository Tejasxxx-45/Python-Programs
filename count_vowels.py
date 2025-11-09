# Program 2: Count vowels in a string
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = sum(1 for ch in string if ch in vowels)
print("Number of vowels:", count)