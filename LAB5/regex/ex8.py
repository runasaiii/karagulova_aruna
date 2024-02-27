import re
def split_at_uppercase(text):
    split_list = re.findall('[A-Z][^A-Z]*', text)
    return split_list


input_string = input("some str:")
result = split_at_uppercase(input_string)
print("Original string:", input_string)
print("Split result:", result)
