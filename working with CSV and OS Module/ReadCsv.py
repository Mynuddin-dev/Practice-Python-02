# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:25:00 2020

@author: Mynuddin
"""

#-------------------------- Reading a CSV file ------------------------------

import  csv

with open("file.csv","r") as f:
    a = csv.reader(f)
    #print(a)
    for line in a:
        print(line)
  
    
with open("file.csv","r") as f:
    a = csv.reader(f)
    next(a)
    for line in a:
        print(line)
        
# with DictReader  ---> OrderedDict
    
with open("file.csv","r") as f:
    a = csv.DictReader(f)
    for line in a:
        print(line)
f.closed

with open("file.csv","r") as f:
    a = csv.DictReader(f , delimiter = ",")
    for line in a:
        print(line)
        
        
        
        
 # csv write

from csv import  writer
with open("file2.csv","w",newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["name","country"])
    csv_writer.writerow(["Mohit","India"])
    csv_writer.writerow(["Byzid","Bangladesh"])
    
    
    #csv_writer.writerows([["name","country"],["Mohit","India"],["Byzid","Bangladesh"]])
               
        
        


# importing the csv module 
import csv 
  
# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
  
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
  
# name of csv file 
filename = "university_records.csv"
  
# writing to csv file 
with open(filename, 'w' ,newline="") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)        
        
        
        
    
        
        
#----------------------------- Writing to a CSV file -------------------------
        
    
        
# my data rows as dictionary objects 
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}] 
  
# field names 
fields = ['name', 'branch', 'year', 'cgpa'] 
  
# name of csv file 
filename = "university_records2.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
      
    # writing headers (field names) 
    writer.writeheader() 
      
    # writer.writerow({'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2')
    #as like that
    
    # writing data rows 
    writer.writerows(mydict)         
        
# https://www.geeksforgeeks.org/working-csv-files-python/     
        
        
        
        
        
        
        
        
        