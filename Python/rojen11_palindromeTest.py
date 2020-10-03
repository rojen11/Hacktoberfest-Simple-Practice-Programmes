// check for palindrome

string = input("Enter a string: ")

if string.lower() == string[::-1].lower():
    print("It is palindrome.")
else:
    print("It is not palindrome.")
