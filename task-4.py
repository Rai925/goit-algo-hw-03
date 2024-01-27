from datetime import datetime, timedelta

users = [
    {"name": "Anne Stuart", "birthday": "1665.02.06"},
    {"name": "Clark Gable", "birthday": "1901.02.01"},
    {"name": "John Joseph Travolta", "birthday": "1954.02.18"},
    {"name": "Dwayne Douglas Johnson", "birthday": "1972.05.02"}
]

def get_upcoming_birthdays(users=None):
    tdate = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        bdate = datetime.strptime(f"{tdate.year}-{user['birthday'][5:]}", "%Y-%m.%d").date()
        days_between = (bdate - tdate).days
        week_day = bdate.isoweekday()

        if 0 <= days_between < 7 and (week_day < 6 or (bdate + timedelta(days=(1 if week_day == 6 else 2))).weekday() == 0):
            formatted_birthday = bdate.strftime("%d %B").replace(" 0", " ")
            upcoming_birthdays.append(f"{user['name']} {formatted_birthday}")

    return upcoming_birthdays

print(get_upcoming_birthdays(users))
