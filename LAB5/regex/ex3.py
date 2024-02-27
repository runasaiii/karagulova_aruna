import re
def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+' 
    matches = re.findall(pattern, text)
    return matches

s = input("Enter some text: ")
sequences = find_sequences(s)
if sequences:
    print("Sequences found:", sequences)
else:
    print("No sequences found.")
