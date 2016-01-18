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
database = client.students
collection = database.grades


# #Connect to the Database
print " --- Return all documents --- "
# #find() returns a cursor in python
# print list(collection.find())
# print len(list(collection.find()))


dict_homework = {}

for var_json in list(collection.find()):
	# print var_json
	# print "\n"
	if var_json["type"] == "homework":
		# print var_json["student_id"], var_json["score"] 
		dict_homework.setdefault(var_json["student_id"], []).append({var_json["score"] : var_json})

for k,v in dict_homework.iteritems():
	# for ele in v:
	# 	print k,ele, ele.values()[0]["score"]


	print int(min([i.keys()[0] for i in v]))
	for ele in v:
		print k,ele, ele.values()[0]["score"]
		if int(ele.values()[0]["score"]) == int(min([i.keys()[0] for i in v])):
			print " --- Removing --- "
			print ele.values()[0]
			collection.remove(ele.values()[0])

	print "\n\n"

