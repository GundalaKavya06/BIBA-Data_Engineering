#continue
for letter in 'HexwareforHexware': 
    if letter == 'e' or letter == 's': 
        continue
    print('Current Letter :', letter) 

#continue
for i in range(1, 11):
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        print(i, end = " ")
 
#break   
for i in range(1, 5):
    for j in range(2, 6):
        # break the loop if
        # # j is divisible by i
        if j%i == 0:
            break
        
        print(i," ", j)
    

#break
for letter in 'HexwareforHexware': 
    if letter == 'e' or letter == 's': 
        break
  
    print('Current1 Letter :', letter) 


#pass
for letter in 'HexwareforHexware': 
    pass
print('Last Letter :', letter) 

#pass - null operation
s = "geeks"
for i in s:
    # No error will be raised
    pass
for i in s:
    if i == "k":
        print("Pass executed")
        pass
    print(i)