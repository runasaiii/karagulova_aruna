import os
file = open('p_tasks\\ex4\\file.txt', 'r')
line_count = 0
while file.readline():
    line_count += 1
print(f"Number of lines: {line_count}")
file.close()
