def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
even_numbers = even_numbers_generator(n)
even_numbers_str = ', '.join(map(str, even_numbers))
print(f"Even numbers between 0 and {n}: {even_numbers_str}")
