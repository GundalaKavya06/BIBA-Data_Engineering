#Slicing - (start index: end index: jump )
list1=[1,2,3,4,5,6,7,8,9]

print(list1[1:])
print(list1[::])
print(list1[::2])
print(list1[4:9:3])
print(list1[::-1])
print(list1[-8:-4:1])
#creating new list
newList = list1[:3]+list1[7:]

#changing exiting list
list1 = list1[::2]+list1[1::2]

print(list1,newList)