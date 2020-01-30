#David "Snake" Wang
#Joseph Yusufov
#Soft Dev Pd 2
#24_rest
#2019-11-12

from flask import Flask, render_template
import urllib, json
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
    u = urllib.request.urlopen(
    "https://api.nasa.gov/planetary/apod?api_key=fQ5u02rjFLFPZQbMTdtwNbjoZnLH6FnBrkV8v450"
    )
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic = data['url'])
    print(__name__) #where will this go?
    return "No hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
