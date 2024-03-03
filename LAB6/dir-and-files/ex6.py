import os
for i in range(ord("A"), ord("Z") + 1):
    file = open(f'PP2\\LABS\\LAB6\\p_tasks\\ex6\\Text Files\\{chr(i)}.txt', 'w')
    file.write(f"This is the {chr(i)}.txt file.")
    file.close()
print("All done")
