__author__ = "Kartik Kannapur"

# #Import Python Libraries
from pymongo import MongoClient
import json

# #Import Property Files
# import properties as prop
json_properties_file = open("properties.json")
json_properties = json.loads(json_properties_file.read())

# #Connect to the Mongo Database
client = MongoClient(json_properties["host"], json_properties["port"])
auth = client.admin.authenticate(json_properties["username"], json_properties["password"])
database = client.sample
collection = database.kartik_mongodb


# #Connect to the Database
print list(collection.find())