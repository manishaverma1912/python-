import calendar
year = int(input("enter the year:"))
for i in range(1, 13):
    print(calendar.month(year, i))

import calendar
year = int(input("enter the year:"))
print(calendar.calendar(year, 3, 2, 2, 4))

