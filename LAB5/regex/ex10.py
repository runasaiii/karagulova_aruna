def camel_to_snake(camel):
    snake = ''
    for i, char in enumerate(camel):
        if i > 0 and char.isupper():
            snake += '_'
        snake += char.lower()
    return snake

camel = input("some stringg:")
snake = camel_to_snake(camel)
print("Camel case string:", camel)
print("Snake case string:", snake)
