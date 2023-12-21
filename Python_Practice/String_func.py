#Capitalize()
strng = "hEllo good morning!"
print(strng.capitalize()) #Hello good morning!

#count()
strng="sun rises in east"
print(strng.count('s')) #4

#find() - returns index at first occurence
print(strng.find('i')) #5

#lower()
strng='SUN RISES IN EAST'
print(strng.lower()) #sun rises in east

#upper()
strng = "sun rises in east"
print(strng.upper()) #SUN RISES IN EAST

#replace
strng= "sun rises in east"
print(strng.replace('s','t')) #tun ritet in eatt

#join() - The join() is used in Python programming to merge each element of an iterable such as a list, set, etc.,
list1=['sun','rises','in','east']
print((' ').join(list1)) #sun rises in east
