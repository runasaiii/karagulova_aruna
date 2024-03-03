import random
def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


number_list = [random.randint(0,10) for i in range(5)]
result = multiply_numbers(number_list)
print(result)
