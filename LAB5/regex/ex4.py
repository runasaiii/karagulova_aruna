import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'  
    matches = re.findall(pattern, text)
    return matches

s = input("some text: ")
sequences = find_sequences(s)
if sequences:
    print("Sequences found:", sequences)
else:
    print("No sequences")
