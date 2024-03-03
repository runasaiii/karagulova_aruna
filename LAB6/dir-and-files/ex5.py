import os
print(os.getcwd())
list = [i for i in input().split(" ")]
file = open('p_tasks\\ex5\\file.txt', 'w')
for item in list:
    file.write(f"{item}\n")
print("List written to file.")
file.close()
