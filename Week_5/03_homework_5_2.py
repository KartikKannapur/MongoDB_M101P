__author__ = "Kartik Kannapur"

# #Import Python Libraries
from pymongo import MongoClient
import json
from collections import Counter

# #Import Property Files
# import properties as prop
json_properties_file = open("properties.json")
json_properties = json.loads(json_properties_file.read())

# #Connect to the Mongo Database
client = MongoClient(json_properties["host"], json_properties["port"])
# auth = client.admin.authenticate(json_properties["username"], json_properties["password"])

# #Database - test
# #Collection - people
database = client.test
collection = database.zips


# #Connect to the Database
print " --- Return all documents --- "
# #find() returns a cursor in python
# print list(collection.find())
# print (list(collection.find()))
# print list(collection.aggregate([{"$project" : {"comments" : 1}} , {"$limit" : 1}]))
# data = list(collection.aggregate([{"$project" : {"comments" : 1}} , {"$limit" : 5}]))
data = list(collection.aggregate([{"$match" : {"$or" : [{"state" : "CA"}, {"state" : "NY"}]}}]))

for ele in data:
	if ele["pop"] > 25000:
		print ele