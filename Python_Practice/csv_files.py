#Read csv file:
#1.using csv.reader()
#2. using csv.readlines()
#3. using pandas module
#4. using csv.DictReader() 

#1.using csv.reader()
import csv
rows=[]
with open("Salary_data.csv","r") as file:
    type(file)
    csvreader = csv.reader(file)
    header=next(csvreader)
    for line in csvreader:
        rows.append(line)        
print(header)
print(rows)

#2.using csv.readlines()
with open("Salary_data.csv") as file:
    content=file.readlines()
header=content[:1]
data=content[1:]
print(header)
print(data)

#3. using pandas
import pandas as pd
data = pd.read_csv("Salary_data.csv")
print(data)
print(data.columns)
#sprint(data.Salary)


#4. using DictReader()
import csv
with open("Salary_data.csv","r") as data:
    reader=csv.DictReader(data)
    for row in reader:
        print(row)
        
        

#Write to csv file:
#1. using csv.writer()
#2. using writelines()
#3. using Pandas
#4. using csv.DictWriter()


#1. using csv.writer()
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
import csv
filename = 'Students_Data.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data) # 5. write the rest of the data
    

#2.using csv.writelines()
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
filename = 'Student_scores.csv'
with open(filename, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('\n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('\n')
     
     
#3. using pandas
import pandas as pd
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
data = pd.DataFrame(data, columns=header)
data.to_csv('Stu_data.csv', index=False)


#4. using DictWriter()
with open('Students_Data.csv', 'w', newline='') as csvfile:
    data = [{'Name': 'Alex', 'M1 Score': 63, 'M2 Score': 80},
        {'Name': 'Brad', 'M1 Score': 45, 'M2 Score': 56},
        {'Name': 'Joey', 'M1 Score': 85, 'M2 Score': 98}]
    fieldnames = ['Name', 'M1 Score', 'M2 Score'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
