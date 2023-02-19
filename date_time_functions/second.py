"""
11 convert Year/Month/Day to Day of Year in Python.
12 get current time in milliseconds in Python
13 get week number.
14 find the date of the first Monday of a given week.
15 select all the Sundays of a specified year.
16 add year(s) with a given date and display the new date.
17 drop microseconds from datetime.
18 get days between two dates.
19 get the date of the last Tuesday.
20 test the third Tuesday of a month.
"""
import datetime
import time

# 11
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)

# 12
milli_sec = int(round(time.time() * 1000))
print(milli_sec)

# 13
print(datetime.date(2015, 6, 16).isocalendar()[1])

# 14
print(time.asctime(time.strptime("2015 50 1", "%Y %W %w")))


# 15
def all_sundays(year):
    # January 1st of the given year
    dt = datetime.date(year, 1, 1)
    # First Sunday of the given year
    dt += datetime.timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += datetime.timedelta(days=7)


for s in all_sundays(2020):
    print(s)


# 16
def addYears(d, years):
    try:
        # Return same day of the current year
        return d.replace(year=d.year + years)
    except ValueError:
        # If not same day, it will return other, i.e.  February 29 to March 1 etc.
        return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))


print(addYears(datetime.date(2015, 1, 1), -1))
print(addYears(datetime.date(2015, 1, 1), 0))
print(addYears(datetime.date(2015, 1, 1), 2))
print(addYears(datetime.date(2000, 2, 29), 1))

# 17
dt = datetime.datetime.today().replace(microsecond=0)
print()
print(dt)
print()

# 18
a = datetime.date(2000, 2, 28)
b = datetime.date(2001, 2, 28)
print(b - a)

# 19
today = datetime.date.today()
offset = (today.weekday() - 1) % 7
last_tuesday = today - datetime.timedelta(days=offset)
print(last_tuesday)


# 20
def is_third_tuesday(s):
    d = datetime.strptime(s, "%b %d, %Y")
    return d.weekday() == 1 and 14 < d.day < 22


print(is_third_tuesday("Jun 23, 2015"))
print(is_third_tuesday("Jun 16, 2015"))
print(is_third_tuesday("Jul 21, 2015"))
