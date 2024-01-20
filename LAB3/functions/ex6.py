def reversed_list(str_list):
    reversed_str = ""
    i = len(str_list) - 1
    while i >= 0:
        reversed_str += str_list[i] + " "
        i -= 1
    return reversed_str.strip()

strr = input("Enter a string: ")
str_list = [elem for elem in strr.split()]
result = reversed_list(str_list)
print(result)
