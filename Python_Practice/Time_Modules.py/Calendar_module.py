#Getting Calendar of a month
import calendar
cal = calendar.month(2023, 12)
print ("Here is the calendar:")
print (cal)

print(calendar.calendar(2024))

print(calendar.isleap(2023)) #False

print(calendar.leapdays(2000,2023)) #returns no. of leap days with in range of 2000-2023
