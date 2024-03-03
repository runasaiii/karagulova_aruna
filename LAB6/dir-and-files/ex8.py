import os
file_path = input("path: ")  
if os.path.exists(file_path):
    print(f"The file {file_path} exists.")
    directory, filename = os.path.split(file_path)
    print(f"Directory: {directory}")
    if os.path.isfile(file_path):
        print(f"Filename: {filename}")
        os.remove(file_path)
        print(f"The file {file_path} has been deleted.")
    else:
        print("No files are in this path.")
else:
    print(f"{file_path} does not exist.")
