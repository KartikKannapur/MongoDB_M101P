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
	return "Hello World!"


@route('/testpage')
def test_page():
	return "This is a Test Page!"

bottle.debug(True)
bottle.run(host='localhost', port=8080)