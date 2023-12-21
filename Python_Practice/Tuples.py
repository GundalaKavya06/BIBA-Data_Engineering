#Tuples - ordered, immutable(unchangeable), duplicates allowed

mytuple = ('apple','banana','orange',1,2,3,True,False)

mtuple = ('apple',) #for one element in a tuple it is necessary to mention comma(,)
print(type(mtuple)) #<class 'tuple'>
stuple = ('apple') 
print(type(stuple)) # <class 'str'>
print(len(mytuple)) #8


#Accessing tuple elements
#indices are started from 0 and -ve indices from -1
print(mytuple[1]) #banana
print(mytuple[1:3]) #('banana', 'orange')
print(mytuple[2:6:2]) #('orange', 2)

if 'banana' in mytuple:
    print(mytuple) #('apple', 'banana', 'orange', 1, 2, 3, True, False)


#changing values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #('apple', 'kiwi', 'cherry')


#Appending values
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')


#adding tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')


#Removing elements
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) 
print(thistuple) #('banana', 'cherry')


#del mytuple - deletes the entire tuple


#adding 2 tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) #('a', 'b', 'c', 1, 2, 3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


