#lists - ordered, changeable, duplicates allowed
mylist= ['apple','orange','watermelon',1,2,3,True,False]

mlist = ['apple']
print(type(mlist)) #<class 'list'>
print(len(mylist)) #8
#Accessing lists
#indices are started from 0 and -ve indices from -1
print(mylist[1:3])  # 1 is included and 3 is excluded o/p:['orange', 'watermelon']
print(mylist[-4:-1]) #[2, 3, True]
print(mylist[2:5]) #['watermelon', 1, 2]

if 'watermelon' in mylist:
    print(mylist) #['apple', 'orange', 'watermelon', 1, 2, 3, True, False] 


#changing list items
mylist[2]='banana'
print(mylist) #['apple', 'orange', 'banana', 1, 2, 3, True, False]

mylist[2:4] = ['kiwi'] #indices 2,3 values are changed to 'kiwi'
print(mylist) #['apple', 'orange', 'kiwi', 2, 3, True, False]

mylist.insert(3,8) #inserting value '8' in the 3rd index but does not change the value of 3rd index it adds up
print(mylist) #['apple', 'orange', 'kiwi', 8, 2, 3, True, False]

#Adding list items
mylist.append('peach')
print(mylist) #['apple', 'orange', 'kiwi', 8, 2, 3, True, False, 'peach']
 # to add 2 lists
demo_list = ['good','morning']
mylist.extend(demo_list)
print(mylist) #['apple', 'orange', 'kiwi', 8, 2, 3, True, False, 'peach', 'good', 'morning']

#removing list items
mylist.remove('peach')
mylist.pop() # deletes last value
del mylist[0] #deletes first value
#del mylist - deletes entire list
#mylist.clear() - deletes the values but not the list
print(mylist) #['orange', 'kiwi', 8, 2, 3, True, False, 'good']


#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#sorting list
fruits.sort() #['apple', 'banana', 'mango']
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) # or thislist.reverse()
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']
