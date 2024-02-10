from datetime import datetime

def drop(dt):
    without = dt.replace(microsecond=0)
    return without

current_datetime = datetime.now()
result = drop(current_datetime)
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", result)
