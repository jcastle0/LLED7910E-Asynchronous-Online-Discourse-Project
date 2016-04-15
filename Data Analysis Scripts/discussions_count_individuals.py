from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.discuss.find({})
userSet = set()
count = 0

for item in items:
	# User Variables
	userId = str(item['userIdEncrypt'])
	userSet.add(userId)
	count += 1

print(len(userSet))
print(count)
print(float(count) / float(len(userSet)))