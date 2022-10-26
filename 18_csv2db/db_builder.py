'''
Metamorphosis: Eric Sohel, Yuki Feng, Maya Mori, Aleksandra Shifrina
SoftDev
k18 -- sqlite in Python
2022-10-25
time spent: 0.8 
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
# c.execute('')
#==========================================================
# with open('students.csv') as f:
#     students_dict = csv.DictReader(f)
#     for row in students_dict:
#         print(row)

# print(students_dict['name'])

#command = "create table students(name text, age int, id int);"

c.execute('create table if not exists students (name text, age int, id int);')
c.execute('create table if not exists courses (code text, mark int, id int);')

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


