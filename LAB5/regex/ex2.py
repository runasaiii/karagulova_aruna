import re
def match_pattern(text):
    pattern = r'ab{2,3}' 
    match = re.fullmatch(pattern, text)
    if match:
        print("String matches")
    else:
        print("String does not match")

s = input("some string: ")
match_pattern(s)
