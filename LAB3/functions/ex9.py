import math
def volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

radius = float(input("Enter the radius of the sphere: "))
volume = volume_of_sphere(radius)
print(f"The volume of the sphere with radius {radius} is {volume}")
