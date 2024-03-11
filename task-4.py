from datetime import datetime, timedelta

users = [
    {"name": "Anne Stuart", "birthday": "1665.02.06"},
    {"name": "Clark Gable", "birthday": "1901.02.01"},
    {"name": "John Joseph Travolta", "birthday": "1954.02.18"},
    {"name": "Dwayne Douglas Johnson", "birthday": "1972.05.10"},
    {"name": "Taras Shevchenko", "birthday": "1814.03.09"},
    {"name": "Carlos Ray Norris", "birthday": "1940.03.10"}
]

def get_upcoming_birthdays(users=None):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        bdate = datetime.strptime(user['birthday'], "%Y.%m.%d").date().replace(year=today.year)
        if 0 <= (bdate - today).days < 7:
            if bdate.weekday() in [5, 6]:
                days_until_monday = (7 - bdate.weekday()) % 7
                bdate += timedelta(days=days_until_monday)
            formatted_birthday = bdate.strftime("%d %B")
            upcoming_birthdays.append(f"{user['name']} {formatted_birthday}")
    return upcoming_birthdays
print(get_upcoming_birthdays(users))
