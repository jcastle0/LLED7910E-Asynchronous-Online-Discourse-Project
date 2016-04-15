from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True })

percentBreakdown = {
	"0-25" : 0,
	"26-50" : 0,
	"51-75" : 0,
	"76-100" : 0
}

totalOp = 0
orphanOp = 0

for item in items:
		percentOrphan = item['percentOrphan']
		orphanOp = item['orphanOp']
		totalOp = item['totalOp']

		if percentOrphan < .26:
			percentBreakdown["0-25"] += 1
		elif percentOrphan < .51:
			percentBreakdown["26-50"] += 1
		elif percentOrphan < .76:
			percentBreakdown["51-75"] += 1
		else:
			percentBreakdown["76-100"] += 1

percentOverall = float(orphanOp) / float(totalOp)

print(percentBreakdown)
print(percentOverall)