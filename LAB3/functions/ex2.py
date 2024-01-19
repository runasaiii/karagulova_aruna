def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


F = float(input("Enter the value of Fahrenheit temperature: "))
C = fahrenheit_to_celsius(F)
print(C)
