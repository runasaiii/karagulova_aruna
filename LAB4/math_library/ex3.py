import math
num=int(input("Input number of sides: "))
len=int(input("Input the length of a side: "))
res=(len**2*num)/(4*math.tan(math.pi/num))
print(res)
