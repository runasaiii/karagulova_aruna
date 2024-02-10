from datetime import datetime, timedelta

def print_dates():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
    print("Today:", today.strftime("%Y-%m-%d"))
    print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))


print_dates()
