import os
path = input("path: ")  
print("Directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

print("Files: ")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

print("Directories and Files: ")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print('Directory: ', os.path.join(dirpath, dirname))
    for filename in filenames:
        print('File:', os.path.join(dirpath, filename))
