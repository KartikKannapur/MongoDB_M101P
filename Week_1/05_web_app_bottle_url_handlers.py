__author__ = "Kartik Kannapur"

# #Import Python Libraries
from pymongo import MongoClient
import json
import bottle
from bottle import route, run, template

# #Import Property Files
# import properties as prop
json_properties_file = open("properties.json")
json_properties = json.loads(json_properties_file.read())


# #Decorators to setup URLs for the web server to listen to
@route('/')
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach']
    return template('hello_world', {'username':"Kartik Kannapur", 'things':mythings})


@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"

    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")

    return bottle.template('fruit_selection.tpl', {'fruit':fruit})


bottle.debug(True)
bottle.run(host='localhost', port=8083)
