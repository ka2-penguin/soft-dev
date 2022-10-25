#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
# with open('students.csv') as f:
#     students_dict = csv.DictReader(f)
#     for row in students_dict:
#         print(row)

# print(students_dict['name'])

#command = "create table students(name text, age int, id int);"
with open('students.csv') as f:
    students_dict = csv.DictReader(f)
    for row in students_dict:
        command = 'insert into students values(' + "\'" + row['name'] + "\'," + row['age'] +',' +  row['id'] +');'
        #print(command)
        c.execute(command)



with open('courses.csv') as f:
    courses_dict = csv.DictReader(f)
    for row in courses_dict:
        command = 'insert into courses values(' + "\'" + row['code'] + "\'," + row['mark'] +',' +  row['id'] +');'
        #print(command)
        c.execute(command)


#==========================================================

db.commit() #save changes
db.close()  #close database


