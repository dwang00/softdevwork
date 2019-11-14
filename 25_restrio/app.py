#David "Snake" Wang
#Soft Dev Pd 2
#25_restrio
#2019-11-13

from flask import Flask, render_template, url_for
import urllib, json
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/jikan")
def jikan():
    u = urllib.request.urlopen(
    "https://api.jikan.moe/v3/anime/5680"
    )
    response = u.read()
    data = json.loads(response)
    return render_template("jikan.html",
        title = data['title'],
        synopsis = data['synopsis'],
        image = data['image_url'],
        episodes = data['episodes'],
        premiered = data['premiered'])

@app.route("/ghibliapi")
def ghibliapi():
    u = urllib.request.urlopen(
    "https://ghibliapi.herokuapp.com/films?title=The%20Wind%20Rises"
    )
    response = u.read()
    data = json.loads(response)
    return render_template("ghibliapi.html",
        title = data[0]['title'],
        description = data[0]['description'],
        director = data[0]['director'],
        producer = data[0]['producer'],
        releasedate = data[0]['release_date'])

@app.route("/pokeapi")
def pokeapi():
    url = "https://pokeapi.co/api/v2/pokemon/gardevoir/"
    request = urllib.request.Request(url)
    request.add_header('User-Agent',"yes")
    u = urllib.request.urlopen(request)
    response = u.read()
    data = json.loads(response)
    return render_template("pokeapi.html", 
        name = data['name'],
        number = data['game_indices'][1]['game_index'],
        type1 = data['types'][1]['type']['name'],
        type2 = data['types'][0]['type']['name'],
        ability1 = data['abilities'][2]['ability']['name'],
        ability2 = data['abilities'][1]['ability']['name'],
        abilityh = data['abilities'][0]['ability']['name'])

if __name__ == "__main__":
    app.debug = True
    app.run()
