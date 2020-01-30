from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def first():
    print(__name__) #where will this go?
    return "TWICE 2018"

@app.route("/1") #assign following fxn to run when root route requested
def what():
    print(__name__) #where will this go?
    return "What is Love?"

@app.route("/2") #assign following fxn to run when root route requested
def dance():
    print(__name__) #where will this go?
    return "Dance the Night Away"

@app.route("/3") #assign following fxn to run when root route requested
def yes():
    print(__name__) #where will this go?
    return "Yes or Yes"

if __name__ == "__main__":
    app.debug = True
    app.run()
