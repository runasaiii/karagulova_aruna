def spy_game(num_list):
    sequence = [0, 0, 7]
    seq_index = 0
    for num in num_list:
        if num == sequence[seq_index]:
            seq_index += 1
            if seq_index == len(sequence):
                return True
    return False

nums = input("Enter numbers of list separated by spaces: ")
num_list = [int(elem) for elem in nums.split()] 
print(spy_game(num_list)) 
