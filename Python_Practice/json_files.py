import json
#json.load(): json.load() function is present in Python built-in ‘JSON’ module. This function is used to parse the JSON string.
#json.loads(): json.loads() function is present in Python built-in ‘json’ module. This function is used to parse the JSON string.
##converting json string to dictionary in python
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
student_details = json.loads(jsonString)
print(student_details)
print(student_details['name'])
print(student_details['course'])


#converting json file to python object
import json
with open('data.json') as json_file:
    data = json.load(json_file)
    print("Type:", type(data))
    print("\nPeople1:", data['people1'])
    print("\nPeople2:", data['people2'])



#json.dumps()
##converting dictionary to json string
import json
dictionary = {
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
print(json_object)



##Converting json to csv
import json   
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
def generate_csv_data(data: dict) -> str:   
    # Defining CSV columns in a list to maintain 
    # the order 
    csv_columns = data.keys()   
    # Generate the first row of CSV  
    csv_data = ",".join(csv_columns) + "\n"  
    # Generate the single record present 
    new_row = list() 
    for col in csv_columns: 
        new_row.append(str(data[col]))   
    # Concatenate the record with the column information  
    # in CSV format 
    csv_data += ",".join(new_row) + "\n" 
    return csv_data   
def write_to_file(data: str, filepath: str) -> bool:   
    try: 
        with open(filepath, "w+") as f: 
            f.write(data) 
    except: 
        raise Exception(f"Saving data to {filepath} encountered an error")   
def main(): 
    # Read the JSON file as python dictionary 
    data = read_json(filename="article.json")   
    # Normalize the nested python dict 
    new_data = normalize_json(data=data)   
    # Pretty print the new dict object 
    print("New dict:", new_data)   
    # Generate the desired CSV data  
    csv_data = generate_csv_data(data=new_data)   
    # Save the generated CSV data to a CSV file 
    write_to_file(data=csv_data, filepath="data.csv") 
if __name__ == '__main__': 
    main()



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
