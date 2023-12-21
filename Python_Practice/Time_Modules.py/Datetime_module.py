from datetime import date
from datetime import datetime
date1 = date(2023, 4, 19)
print("Date:", date1)
date2 = date(2023, 12, 31)

# Getting min date
mindate = date.min
print("Minimum Date:", mindate)


# Getting max date
maxdate = date.max
print("Maximum Date:", maxdate)


Date1 = date(2023, 4, 20)
print("Year:", Date1.year)
print("Month:", Date1.month)
print("Day:", Date1.day)

dt = datetime.now()
print("Day Name:",dt.strftime('%A'))