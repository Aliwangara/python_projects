import datetime

now = datetime.datetime.now()

activity_log = "activity_log.txt"




with open(activity_log, 'a') as f:
    while True:
        todays_activity_input = input("Enter activity: ")
        f.write(f"[{now}] - {todays_activity_input}\n")
        print("✅ Activity logged!")

        log_another_activity = input("Enter another activity? (y or n)").lower()

        if log_another_activity != "y":
            break





with open(activity_log,"r") as f:
    print("📘 All Logged Activities:")
    print(f.read())

    

