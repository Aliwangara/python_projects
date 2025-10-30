import datetime

current_date = datetime.datetime.now()
print(f"Current Date: {current_date}")

current_time = datetime.datetime.now().time()
print(f"Current Time: {current_time}")

today = datetime.date.today()
print(f"Today: {today}")

birthday = datetime.date(2004,8,5)

print("Birthday: ", birthday)

now = datetime.datetime.now()

formatted = now.strftime("%D-%M-%Y %H:%M:%S")

print("Formatted hours: ", formatted)

exam_date = datetime.date(2026,1,1)

remaining = exam_date - today

print("Remaining Days: ", remaining)