def grams_to_ounces(grams):
    return grams * 28.3495231


x = float(input("Enter the value of gram: "))
result = grams_to_ounces(x)
print(result)
