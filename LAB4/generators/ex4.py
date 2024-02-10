def squares(a,b):
    for i in range(a, b + 1, 1):
        yield i**2


a,b = map(int,input().split())

numbers = squares(a,b)
numbers_str = ', '.join(map(str, numbers))
print(f"Square of all numbers from {a} to {b}: {numbers_str}")
