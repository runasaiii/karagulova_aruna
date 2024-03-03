def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]


s = input("string: ")
if is_palindrome(s):
    print("palindrome.")
else:
    print("not palindrome.")
