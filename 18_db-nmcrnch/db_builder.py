#David Wang
#SoftDev pd2
#K18 Average
#2019-10-14

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
from csv import DictReader

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

file = DictReader(open("students.csv"))
c.execute("DROP TABLE IF EXISTS students;") #deletes previous instance of table
c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);") #creates table students
for row in file: #takes values from csv and puts it into string "values"
    values = ""
    z = 0 #counter
    for x in row.values():
        if z == 0:
            values = values + "\"" + x + "\"" + ", " #puts quotes around first value to make it a "string"
            z += 1
        else:
            values = values + x + ", "
    values = values[:-2] #removes comma and space from end of values
    c.execute("INSERT INTO students VALUES (" + values + ");") #adds values to table

file = DictReader(open("courses.csv"))
c.execute("DROP TABLE IF EXISTS courses;") #deletes previous instance of table
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);") #creates table courses
for row in file: #takes values from csv and puts it into string "values"
    values = ""
    z = 0 #counter
    for x in row.values():
        if z == 0:
            values = values + "\"" + x + "\"" + ", " #puts quotes around first value to make it a "string"
            z += 1
        else:
            values = values + x + ", "
    values = values[:-2] #removes comma and space from end of values
    c.execute("INSERT INTO courses VALUES (" + values + ");") #adds values to table

#==========================================================

db.commit() #save changes
db.close()  #close database
