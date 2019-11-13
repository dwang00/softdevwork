#David "Snake" Wang
#Soft Dev Pd 2
#25_restrio
#2019-11-12

from flask import Flask, render_template
import urllib, json
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
    u = urllib.request.urlopen(
    "https://api.jikan.moe/v3/anime/5680"
    )
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", title = data['title'], synopsis = data['synopsis'], image = data['image_url'])
    print(__name__) #where will this go?
    return "No hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
