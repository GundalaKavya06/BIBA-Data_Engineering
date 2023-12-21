import numpy as np
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] )  
print("Array is of type: ", type(arr))   #<class 'numpy.ndarray'>
print("No. of dimensions: ", arr.ndim)  #2
print("Shape of array: ", arr.shape)  #(2,3)
print("Size of array: ", arr.size)  #6
print("Array stores elements of type: ", arr.dtype)  #int 32



#Numpy Array Creation
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 
# [[1. 2. 4.]
# [5. 8. 7.]]
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b) #[1 3 2]



c = np.zeros((3, 4)) 
print ("An array initialized with all zeros:\n", c) 
d = np.full((3, 3), 6, dtype = 'complex') 
print ("An array initialized with all 6s." 
            "Array type is complex:\n", d) 
e = np.random.random((2, 2)) 
print ("A random array:\n", e)



#arange # Create a sequence of integers from 0 to 30 with steps of 5. Step size is specified
f = np.arange(0, 30, 5) 
print ("A sequential array with steps of 5:\n", f)


#linspace #It returns evenly spaced values within a given interval.
g = np.linspace(0, 5, 10) 
print ("A sequential array with 10 values between"
                                 "0 and 5:\n", g)


#Reshape
arr = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]])  
newarr = arr.reshape(2, 2, 3)  
print ("Original array:\n", arr) 
print(newarr)


#Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
flat_arr = arr.flatten()
print ("Original array:\n", arr) 
print ("Fattened array:\n", flat_arr)


#Numpy Array Indexing - Slicing, Integer array indexing, Boolean array indexing
arr = np.array([[-1, 2, 0, 4], 
                [4, -0.5, 6, 0], 
                [2.6, 0, 7, 8], 
                [3, -7, 4, 2.0]])  
# Slicing array 
temp = arr[:2, ::2] 
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp) 
# Integer array indexing example 
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),(3, 0):\n", temp) 
# boolean array indexing example 
cond = arr > 0 # cond is a boolean array 
temp = arr[cond] 
print ("\nElements greater than 0:\n", temp)  




#Numpy Operations
a = np.array([1, 2, 5, 3]) 
# add 1 to every element 
print ("Adding 1 to every element:", a+1) 
# subtract 3 from each element 
print ("Subtracting 3 from each element:", a-3) 
# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 
# square each element 
print ("Squaring each element:", a**2)  
# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 
# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 



#Numpy Unary operations
arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 
# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", 
                    arr.max(axis = 1)) 
# minimum element of array 
print ("Column-wise minimum elements:", 
                        arr.min(axis = 0)) 
# sum of array elements 
print ("Sum of all array elements:", 
                            arr.sum()) 
# cumulative sum along each row 
print ("Cumulative sum along each row:\n", 
                        arr.cumsum(axis = 1)) 




#Numpy Binary operations 
a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[4, 3], 
            [2, 1]])  
# add arrays 
print ("Array sum:\n", a + b) 
# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b)  
# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 


#Numpy universal functions
# create an array of sine values 
a = np.array([0, np.pi/2, np.pi]) 
print ("Sine values of array elements:", np.sin(a)) 
# exponential values 
a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 
# square root of array values 
print ("Square root of array elements:", np.sqrt(a)) 




#Numpy Sorting arrays
a = np.array([[1, 4, 2], 
                 [3, 4, 6], 
              [0, -1, 5]]) 
# sorted array 
print ("Array elements in sorted order:\n", 
                    np.sort(a, axis = None))  
# sort array row-wise 
print ("Row-wise sorted array:\n", 
                np.sort(a, axis = 1))  
# specify sort algorithm 
print ("Column wise sort by applying merge-sort:\n", 
            np.sort(a, axis = 0, kind = 'mergesort')) 
# Example to show sorting of structured array 
# set alias names for dtypes 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]  
# Values to be put in array 
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),  
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]            
# Creating array 
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", 
            np.sort(arr, order = 'name'))               
print ("Array sorted by graduation year and then cgpa:\n", 
                np.sort(arr, order = ['grad_year', 'cgpa'])) 
