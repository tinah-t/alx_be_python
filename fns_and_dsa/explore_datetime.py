from datetime import datetime,date
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date_formatted=current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date_formatted}")



def calculate_future_date():
    current_date = date.today()
    future_date = int(input("Enter the number of days to add to the current date: "))
    result= current_date+timedelta(future_date)
    print(f"Future date: {result}")

display_current_datetime()
calculate_future_date()