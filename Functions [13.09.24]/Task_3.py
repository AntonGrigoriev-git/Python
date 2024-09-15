'''The date of a certain day.'''

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

# месяца с 30-ю днями
months = [4, 6, 9, 11]

if year < 1:
    raise ValueError("Invalid year! Please enter a positive year.")

if month < 1 or month > 12:
    raise ValueError("Invalid month! Please enter a month between 1 and 12.")

if month in months:
    max_day = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_day = 29
    else:
        max_day = 28
else:
    max_day = 31

if day < 1 or day > max_day:
    raise ValueError(f"Invalid day! Please enter a day between 1 and {max_day}.")


def previous_day(day, month, year):
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            year -= 1
            month = 12
        if month in months:
            day = 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day = 29
            else:
                day = 28
        else:
            day = 31
    return f"Date of the previous day {day:02}.{month:02}.{year}."


def next_day(day, month, year):
    if month in months:
        max_day = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        max_day = 31

    day += 1
    if day > max_day:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"Date of the next day {day:02}.{month:02}.{year}."


def days_in_month(month, year):
    if month in months:
        days = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        else:
            days = 28
    else:
        days = 31
    return f"The number of days in a month is equal to {days}."

print(previous_day(day, month, year))
print(next_day(day, month, year))
print(days_in_month(month, year))