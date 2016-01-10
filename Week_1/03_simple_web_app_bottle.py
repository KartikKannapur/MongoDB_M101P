__author__ = "Kartik Kannapur"

# #Import Python Libraries
from pymongo import MongoClient
import json
from bottle import route, run, template

# #Import Property Files
# import properties as prop
json_properties_file = open("properties.json")
json_properties = json.loads(json_properties_file.read())


# #Decorators to setup URLs for the web server to listen to
@route('/')
def index():
	# #Connect to the Mongo Database
	client = MongoClient(json_properties["host"], json_properties["port"])
	auth = client.admin.authenticate(json_properties["username"], json_properties["password"])
	database = client.sample
	collection = database.kartik_mongodb

	data = list(collection.find())
	return template('<b>Data in MongoDB : {{var_data}}</b>', var_data=data)


run(host='localhost', port=8081)