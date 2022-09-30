"""
Humans: Maya Mori, Justin Mohabir
Duckies: Catbat, Alfred
Softdev
06_py-csv
2022-09-29
time spent: 1.0 hr
DISCO:
  - TypeError: 'dict_keys' object is not subscriptable
  - csv.reader(some_csv_file) will separate the values and deals with extra
  commas andquotation marks
  - random.choices() can return random values that are weighted
QCC:

HOW THIS SCRIPT WORKS:
  - We read the file using csv.reader() into data with each row in a list
  - We created a dictionary with occupation as the key and the percentage as
  the value
  - Then, we used random.choices() in random_occupation to get a weighted
  random occupation

"""

import random as rg

import csv

data1 = []
data = []

with open('occupations.csv','r') as csvfile:
    #data = list(csv.reader(csvfile))
    data0 = csvfile.read().split('\n')
    for row in data0:
        data1 += [row.split("\"")]
        
for row in data1:
    if len(row) == 1:
        data += [row[0].split(',')]
    else:
        data += [[row[1],row[-1][1:]]]

print(data)



data = data[1:-2]

dict_data = {}
tester = {}

for row in data:
    dict_data[row[0]] = float(row[1])
    tester[row[0]] = 0

print(dict_data)

def random_occupation():
    return rg.choices(list(dict_data.keys()),\
           weights=list(dict_data.values()))[0]

#tester = {}

for i in range(1000000):
    occ = random_occupation()
    if occ not in tester:
        tester[occ] = 0
    tester[occ] += 1
    
print(tester)

'''
l = [1,2,3]
w = [1.0,2.0,3.5]

for i in range(10):
    print(rg.choices(l,weights=w))
    
data = {1:0,2:0,3:0}

for i in range(100000):
    data[rg.choices(l,weights=w)[0]] += 1

print(data)
'''

