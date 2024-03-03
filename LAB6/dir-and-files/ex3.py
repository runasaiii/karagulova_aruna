import os
path = input("path: ")  
if os.path.exists(path):
    print(f"{path} exists.")
    directory, filename = os.path.split(path)
    print(f"Directory: {directory}")
    if os.path.isfile(path):
        print(f"Filename: {filename}")
    else:
        print("No files are in this path.")
else:
    print(f"{path} does not exist.")
