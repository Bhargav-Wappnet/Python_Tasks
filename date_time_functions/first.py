"""
1  display the various Date Time formats
2 determine whether a given year is a leap year.
3 convert a string to datetime.
4 get the current time in Python.
5 subtract five days from current date.
6 convert unix timestamp string to readable date.
7 print yesterday, today, tomorrow.
8 convert the date to datetime (midnight of the date) in Python.
9 print next 5 days starting from today.
10 add 5 seconds with the current time.
"""
import datetime

# 1
print("Current date and time: ", datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))


# 2
def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False


print(leap_year(1900))
print(leap_year(2004))

# 3
date_object = datetime.strptime("Jul 1 2014 2:43PM", "%b %d %Y %I:%M%p")
print(date_object)

# 4
print(datetime.datetime.now().time())

# 5
dt = datetime.date.today() - datetime.timedelta(5)
print("Current Date :", datetime.date.today())
print("5 days before Current Date :", dt)

# 6
print(datetime.datetime.fromtimestamp(int("1284105682")).strftime("%Y-%m-%d %H:%M:%S"))

# 7
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday : ", yesterday)
print("Today : ", today)
print("Tomorrow : ", tomorrow)

# 8
dt = datetime.date.today()
print(datetime.combine(dt, datetime.min.time()))

# 9
base = datetime.datetime.today()
for x in range(0, 5):
    print(base + datetime.timedelta(days=x))

# 10
x = datetime.datetime.now()
y = x + datetime.timedelta(0, 5)
print(x.time())
print(y.time())
