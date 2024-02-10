from datetime import datetime

def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    difference_in_seconds = difference.total_seconds()

    return difference_in_seconds


date_str1 = "2024-02-01 12:00:00"
date_str2 = "2024-02-10 12:00:00"
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
difference = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference)
