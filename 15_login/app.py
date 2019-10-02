#David "Snake" Wang and Benjamin Avrahami
#SoftDev1 pd2
#K15: Do I Know You?
#2019-10-02

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__) #create instance of class Flask

user = "Gold"
pas = "Potatoes"

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) 
    return render_template('loginpage.html',u=user,p=pas)

@app.route("/auth")
def verify():
	return "Not yet"

if __name__ == "__main__":
    app.debug = True
    app.run()
