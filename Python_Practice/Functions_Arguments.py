##Default Arguments
def myfun(x,y=10):
    print(x,y)

myfun(6)


##Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
student("Hexa", "Practice")
student(lastname='Practice', firstname='Hexa')


##Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
print("Case-1:")
nameAge("Suraj", 27) #Hi, I am Suraj My age is  27
print("\nCase-2:")
nameAge(27, "Suraj") #Hi, I am 27 My age is  Suraj


##Arbitrary Keyword Arguments
# Python program to illustrate *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)
 
myFun('Hello', 'Welcome', 'to', 'HexaforHexa')
#Hello
# Welcome
# to
# HexaforHexa


#Python program to illustrate *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
# Driver code
myFun(first='Hexa', mid='for', last='Hexa')
#first == Hexa
# mid == for
# last == Hexa

