import re
def insert_spaces(text):
    text2 = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    return text2


s = input("some str: ")
result = insert_spaces(s)
print("Original string:", s)
print("Modified string:", result)
