#Operators
a=int(input("enter a:"))
b=int(input("enter b:"))
#Arithmetic Operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)


#Assignment Operators
a+=3
b-=4
a*=3

#Comparision Operators
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical Operators
x=5
print(x>5 and x<9)
print(x>5 or x<9)
print(not(x>5 and x<9))


#Identity Operators - checks if they both referring to same memory
print(a is b)
print(a is not b)

#Membership Operators
mlist=[1,2,3,True,'Apple']
if 'Apple' in mlist:
    print(mlist)

if 4 not in mlist:
    print(mlist)
    

#Bitwise Operators
print(6&3) #AND
print(6|3) #OR
print(6^3) #XOR
print(~3) #NOT
print(3<<2) #Left Shift 
print(3>>2) #Right Shift


#Precedence 
# "()" > "**" > "Unary plus,minus, Bitwise NOT" > "* / // %" > "+ -" > "<< >>" > Comparisions
