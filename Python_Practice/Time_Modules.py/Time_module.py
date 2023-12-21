import time # This is required to include time module.
ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)


#print (time.localtime()) #time.struct_time(tm_year=2023, tm_mon=12, tm_mday=16, tm_hour=10, tm_min=41, tm_sec=53, tm_wday=5, tm_yday=350, tm_isdst=0)


# localtime = time.localtime(time.time())
# print ("Local current time :", localtime) #time.struct_time(tm_year=2023, tm_mon=12, tm_mday=16, tm_hour=10, tm_min=41, tm_sec=53, tm_wday=5, tm_yday=350, tm_isdst=0)


localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime) #Sat Dec 16 10:41:53 2023


print(time.altzone)

print(time.asctime()) #Sat Dec 16 10:56:29 2023
