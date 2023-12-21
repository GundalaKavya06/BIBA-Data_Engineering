amount = 10000
#if(amount > 2999) #syntax error
print("You are eligible to purchase Dsa Self Paced") 

marks = 10000
#a = marks / 0 #ZeroDivison error
#print(a)

x = 5
y = "hello"
#z = x + y #type error


#Exception Handling
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")


##finally
try:
    k = 5//0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('This is always executed')


##raise
try: 
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    raise #reraises an exception
