from itertools import permutations
def print_permutations(strr):
    all_permutations = permutations(strr)
    for perm in all_permutations:
        print(''.join(perm))


strr = input("Enter a string: ")
print_permutations(strr)
