def cube(x): return x*x*x
#lambda function
cube_v2 = lambda x : x*x*x
print(cube(7)) #343
print(cube_v2(7)) #343


str1 = 'HexaforHexa'
upper = lambda string: string.upper()
print(upper(str1)) #HEXAFORHEXA


is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item()) 
# 10
# 20
# 30
# 40


List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
print(res) #[3, 16, 9]


format_numeric =lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000)) #Int formatting: 1.000000e+06
print("float formatting:", format_numeric(999999.789541235)) #float formatting: 999,999.79


#Lambda with reduce() function
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)  #193

 