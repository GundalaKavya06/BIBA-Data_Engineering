# importing the module
import TempConversion
# using a function of the module
print(TempConversion.to_centigrade(12))
# fetching an object of the module
print(TempConversion.FREEZING_F)




##importing a method from module
from TempConversion import to_fahrenheit
# using the imported method
print(to_fahrenheit(20))
# importing the FREEZING_C object
from TempConversion import FREEZING_C
# printing the imported variable
print(FREEZING_C)