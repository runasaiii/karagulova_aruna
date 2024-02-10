def nums(n):
    for i in range(n, 0-1, -1):
        yield i


n = int(input("number n: "))

numbers = nums(n)
for elem in numbers:
    print(elem)
