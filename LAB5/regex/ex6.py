import re
def replace_with_colon(text):
    pattern = r'[ ,.]'  
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text

s = input(soome text: ")
replaced_text = replace_with_colon(s)
print("Original text:", s)
print("Text with replacements:", replaced_text)
