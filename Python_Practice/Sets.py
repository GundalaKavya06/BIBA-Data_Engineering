#Sets - Unordered, Immutable, no Duplictes allowed

myset = {'apple','banana','watermelon',1,2,3,False}
print(myset) 


##no duplictes
set1={1,2,3,3,4}
print(set1) #{1,2,4,3} 

#length of set
print(len(myset)) #7
print(type(myset)) #<class 'set'>

#set is immutable
# set1[1]=2
# print(set1) #throws type error: 'set' object does not support item assignment


##typecasting list to set
myset1 = set(["a", "b", "c"])
print(myset1)


##Frozen sets - While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 
f_set = {'e','f','g','h'}
print(f_set) #{'f', 'e', 'h', 'g'}
f_set.add('apple') #does not add 'apple' to frozen set


##Accessing set elements
#print(myset[1]) #error bcoz set is unordered
if "apple" in myset:
    print(myset) #{False, 1, 2, 3, 'banana', 'apple', 'watermelon'}


##Adding elements to the set
set1.add('apple')
print(set1) #{1, 2, 3, 4, 'apple'}


##Removing set elements
myset.remove('apple') #remove()  gives error if element not found 
print(myset) #{False, 1, 2, 3, 'banana', 'watermelon'}
#discarding
myset.discard('apple')
#pop
myset.pop() #removes a random element
#myset.clear() - empties the set elements
#del myset() - deletes entire set
print(myset) #{1, 2, 'banana', 3, 'watermelon'}


##adding one set to other using update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # the object in update() method can be a list,tuple,set
print(thisset) #{'banana', 'apple', 'papaya', 'cherry', 'mango', 'pineapple'}


##adding one set to other using union()
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
population = people.union(vampires)
print(population) #{'Jay', 'Archil', 'Karan', 'Idrish', 'Arjun'}

#adding one set to other using  '|' operator
population = people|dracula
print(population) #{'Jay', 'Archil', 'Deepanshu', 'Idrish', 'Raju'}


##Intersection in sets
set1 = set()
set2 = set()
for i in range(5):
    set1.add(i)
for i in range(3,9):
    set2.add(i)
# Intersection using intersection() function
set3 = set1.intersection(set2)
print(set3) #{3, 4}
# Intersection using"&" operator
set3 = set1 & set2
print(set3) #{3, 4}


##Finding Differences in sets
#Difference of two sets using difference() function
set3 = set1.difference(set2)
print(set3) #{0, 1, 2}
#Difference of two sets using '-' operator
set3 = set2 - set1
print(set3) #{8, 5, 6, 7}

#isdisjoint 
print(set1.isdisjoint(set2)) #False

set1={1,2,3}
set2={1,2,3,4,5}
#issubset
print(set1.issubset(set2)) #True

#issuperset
print(set2.issuperset(set1)) #True





