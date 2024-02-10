def squares(a,b):
    for i in range(a, b + 1, 1):
        yield i**2


a,b = map(int,input().split())

numbers = squares(a,b)
for elem in numbers:
    print(elem)
