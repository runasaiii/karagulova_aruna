import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'match!'
        else:
                return('not matched!')

s=input("some text: ")
print(text_match(s))
