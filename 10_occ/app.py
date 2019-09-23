#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#demo -- My First Flask App
#2019-09-17t
import random
from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"


diction = {}
def convertToDict():
    ary = []
    file = open('occupations.csv', 'r')
    file.readline()
    for line in file:
        if '"' in line:
            #print(line.split('"')[1:])
            ary.append(line.split('"')[1:])
        #print(line.split(',')[0])
        else:
            ary.append(line.split(','))
    ary = ary[:-1]
    for arr in ary:
        if ',' in arr[1]:
            arr[1] = arr[1][1:]
        #print(arr[1])
        arr[1] = arr[1].replace('\n', '')
        #print(arr)
        diction.update({arr[0]:float(arr[1])})
    #print(diction)
    return ary

def randomJob():
    weightedList = []
    for job in diction:
        weight = int(float(diction[job]) * 10)
        original = weight
        #print(weight)
        while weight > 0:
            weightedList.append(job + ", " + str(float(original) / 10.0))
            #print(weightedList)
            weight = weight - 1
    #print(weightedList)
    return(weightedList[random.randint(0, len(weightedList) - 1)])
@app.route("/occupyflaskst")
def test_tmplt():
   return render_template(
      'model_tmplt.html',
      d = convertToDict(),
      f = randomJob())

if __name__ == "__main__":
    app.debug = True
    app.run()


