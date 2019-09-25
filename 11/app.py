#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#demo -- My First Flask App
#2019-09-17t

from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(app)
    print(request)
    print(request.args)	
    return render_template('form.html')
    #print(__name__) #where will this go?    

if __name__ == "__main__":
    app.debug = True
    app.run()
