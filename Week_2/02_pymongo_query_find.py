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
# auth = client.admin.authenticate(json_properties["username"], json_properties["password"])

# #Database - test
# #Collection - people
database = client.test
collection = database.people


# #Connect to the Database
print " --- Return all documents --- "
# #find() returns a cursor in python
print list(collection.find())

print " --- Find One document --- "
print collection.find_one()

print " --- Find One document with a query condition --- "
query_1 = {"age" : 45}
print collection.find_one(query_1)

# #Projections
print " --- Finding documents with Projections --- "
query_2 = {"age" : 45}
# #SELECT name & I don't want to see _id
projection = {"name" : 1, "_id" : 0}
print list(collection.find(query_2, projection))
