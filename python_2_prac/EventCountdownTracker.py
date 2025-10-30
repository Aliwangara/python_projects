import datetime

event_name = input("Enter event name:  ")
event_date = input("Enter event date. format(YYYY-MM-DD): ")

today = datetime.date.today()
event_conversion = datetime.datetime.strptime(event_date, "%Y-%m-%d").date()

days_left = (event_conversion - today).days

print(f"📅 Event: {event_name}")
print(f"📆 Today’s Date {today}")
print(f"🎉 Event Date: {event_conversion}")
print(f"⏳ Days Remaining: {days_left}")
