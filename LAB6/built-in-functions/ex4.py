import time
import math

def sqr_after_mls(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result


number = 25100
milliseconds = 2123
result = sqr_after_mls(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
