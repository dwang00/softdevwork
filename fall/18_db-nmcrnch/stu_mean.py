#David Wang
#SoftDev pd2
#K18 Average
#2019-10-14

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
from csv import DictReader

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

c.execute("DROP TABLE IF EXISTS averages;") #deletes existing table
c.execute("CREATE TABLE averages(id INTEGER, average INTEGER);") #creates new table for averages

#SUM (mark) / COUNT (mark)

get = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;" #defines and executes way to get values
data = c.execute(get)

names = []
ids = []
marks = []

for row in data: #populates blank lists with names, ids, marks
    if row[0] not in names:
        names.append(row[0])
    ids.append(row[1])
    marks.append(row[2])

counter = 0
current = 0 #current sum of grades
avgs = []
for i in ids: #populates avgs
    if counter == len(ids) - 1: #when element is last in list
        current += marks[counter]
        avgs.append(current / ids.count(ids[counter])) #appends avg (total sum divided by # of times id appears) to avgs
    elif ids[counter] == ids[counter + 1]: #when id of current equals id of next
        current += marks[counter]
        counter += 1
    else: #when id of current doesnt equal id of next
        current += marks[counter]
        avgs.append(current / ids.count(ids[counter]))
        current = 0 #reset current
        counter += 1

counter = 0
for i in avgs: #prints all avgs and adds it to database
    print("name: " + names[counter] + " id: " + str(counter + 1) + " average: " + str(i))
    c.execute("INSERT INTO averages VALUES("+ str(counter + 1) + "," + str(i) + ")")
    counter += 1

db.commit()
db.close()
