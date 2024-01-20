def unique_elements(num_list):
    new_list = []
    for element in num_list:
        if element not in new_list:
            new_list.append(element)
    return new_list

nums =input("Enter the nums: ")
num_list = [int(elem) for elem in nums.split()]
res=unique_elements(num_list)
print(res)
