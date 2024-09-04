import datetime

def days(mo, da, leap):
    if not leap:
        date = datetime.date(2025, mo, da)
        days = date.timetuple().tm_yday

    else:
        date = datetime.date(2024, mo, da)
        days = date.timetuple().tm_yday
    return days

print(days(9, 4, True))