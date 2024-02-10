from datetime import datetime, timedelta

def f():
    current_date = datetime.now()
    five_days_ago = current_date - timedelta(days=5)

    return five_days_ago

result = f()
print("Five days ago from the current date:", result.strftime("%Y-%m-%d"))
