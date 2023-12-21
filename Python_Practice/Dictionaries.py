#Dictionaries - Ordered, Mutable, no duplictes allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


##no duplicates allowed 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020} #overwrites the existing value


##length of dict
print(len(thisdict)) #3
print(type(thisdict)) #<class 'dict'>


#Accessing dictionary items
x=thisdict["model"]
print(x) #Mustang

#Retriving using get() method
print(thisdict.get("model")) #Mustang

#To get keys in a dictionary
print(thisdict.keys()) #dict_keys(['brand', 'model', 'year'])

#To get keys in a dictionary
print(thisdict.values()) #dict_values(['Ford', 'Mustang', 2020])

#To get all itema (keys , values) in the form of a tuple from dictionary
print(thisdict.items()) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

if "model" in thisdict:
    print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
    

##Changing items in a dictionary
thisdict["year"]=2023
print (thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2023}

thisdict.update({"year":2024})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2024}

##Adding items to dictionary
thisdict["color"] = "red"
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'red'}


##Removing items from dictionary
thisdict.pop("model") #specifically deletes "model"

thisdict.popitem()#pops out last item

#thisdict.clear() #empties a dictionary


#del thisdict["model"] #specifically deletes "model"
#del thisdict #deletes entire dictionary


#Looping in dictionaries
for x in thisdict:
  print(thisdict[x]) #Ford #\n2024
  
  
##Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"]) #Tobias





