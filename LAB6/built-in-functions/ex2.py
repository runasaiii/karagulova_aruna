def count(string):
    u_count = sum(1 for char in string if char.isupper())
    l_count = sum(1 for char in string if char.islower())
    return u_count, l_count


s = input("string:")
upper, lower = count(s)
print("uppercase letters:", upper)
print("lowercase letters:", lower)
