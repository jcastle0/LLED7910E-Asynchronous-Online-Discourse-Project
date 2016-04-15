from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

with open('lled_orphans.json') as jsonFile:
	data = json.load(jsonFile)

for d in data:
	for i in d:
		course = i
		topics = d[i]
		courseOrphans = 0
		for t in topics:
			topic = t
			numOrphans = topics[t]
			courseOrphans = courseOrphans + numOrphans
		print(course + ": " + str(courseOrphans))