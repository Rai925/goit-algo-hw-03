import datetime as dt

def get_days_from_today(date):
    try:
        date_obj = dt.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Введіть дату у форматі РРРР-ММ-ДД.")
    
    today = dt.date.today()
    days_diff = (today - date_obj).days
    return days_diff

try:
    date_input = input("Введіть дату у форматі РРРР-ММ-ДД: ")
    days_diff = get_days_from_today(date_input)
    print(f"Кількість днів між введеною датою та поточною: {days_diff} днів")
except ValueError as e:
    print(f"Помилка: {e}")