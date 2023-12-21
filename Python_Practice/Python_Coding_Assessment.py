#1. Explain Python Module with examples
#Module - A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. 

#Some pre defined modules in python
from math import *
import math
print(sqrt(24)) 
print(factorial(7)) 
print(math.pi) 
print(math.degrees(2)) 
print(math.cos(0.5))


#a. renaming a pre defined module 
import random as r
print(r.randint(0,5))
print(r.random())
print(r.random() * 100)  
List = [1, 4, True, 800, "python", 27, "hello"]
print(r.choice(List)) 


#Datetime module
from datetime import date
from datetime import datetime
Date1 = date(2023, 4, 20)
print("Year:", Date1.year)
print("Month:", Date1.month)
print("Day:", Date1.day)
dt = datetime.now()
print("Day Name:",dt.strftime('%A'))




#User-defined modules
import TempConversion
# using a function of the module
print(TempConversion.to_centigrade(12))
# fetching an object of the module
print(TempConversion.FREEZING_F)


#a. renaming the user defined module
from TempConversion import to_fahrenheit as t
# using the imported method
print(t(20))
# importing the FREEZING_C object
from TempConversion import FREEZING_C
# printing the imported variable
print(FREEZING_C)




#2.Explain Pandas and numpy using Examples in PYTHON
#Pandas - Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
#Here we are using .csv and .json files


#Reading and writing .csv files using Pandas
#Reading data from Salary_data.csv
import pandas as pd
data = pd.read_csv("Salary_data.csv")
print(data)
print(data.columns)


#writing data to Stu_data.csv
import pandas as pd
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
data = pd.DataFrame(data, columns=header)
data.to_csv('Stu_data.csv', index=False)


#reading data from .json file
data = pd.read_json("data1.json")
print(data)


#writing data to .json file
df = pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                  index =['row 1', 'row 2', 'row3'],
                  columns =['col 1', 'col 2', 'col3'])
df.to_json('file.json', index = 'true')



##Converting json to csv using pandas
import json 
import pandas 
def read_json(filename: str) -> dict: 
    try: 
        with open(filename, "r") as f: 
            data = json.loads(f.read()) 
    except: 
        raise Exception(f"Reading {filename} file encountered an error") 
    return data   
def normalize_json(data: dict) -> dict:  
    new_data = dict() 
    for key, value in data.items(): 
        if not isinstance(value, dict): 
            new_data[key] = value 
        else: 
            for k, v in value.items(): 
                new_data[key + "_" + k] = v      
    return new_data   
def main(): 
    # Read the JSON file as python dictionary 
    data = read_json(filename="article.json")  
    # Normalize the nested python dict  
    new_data = normalize_json(data=data)  
    print("New dict:", new_data, "\n") 
    # Create a pandas dataframe  
    dataframe = pandas.DataFrame(new_data, index=[0]) 
    # Write to a CSV file 
    dataframe.to_csv("article.csv")   
if __name__ == '__main__': 
    main()






#Numpy- NumPy is a general-purpose array-processing package, providing a high-performance multidimensional array object and tools for working with these arrays.
import numpy as np
#creation of a numpy array
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
print("Array is of type: ", type(arr))   
print("No. of dimensions: ", arr.ndim) 
print("Shape of array: ", arr.shape) 
print("Size of array: ", arr.size)  
print("Array stores elements of type: ", arr.dtype) 

##Reshaping a numpy array
arr = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]])  
newarr = arr.reshape(2, 2, 3)  
print ("Original array:\n", arr) 
print(newarr)

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
