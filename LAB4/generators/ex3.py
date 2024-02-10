def numbers_generator(n):
    for i in range(1, n + 1, 1):
        if i%3==0 and i%4==0:
            yield i


n = int(input("Enter a number: "))

numbers = numbers_generator(n)
numbers_str = ', '.join(map(str, numbers))
print(f"The numbers, which are divisible by 3 and 4, between a given range 0 and {n}: {numbers_str}")
