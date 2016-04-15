from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.discuss.find({})

topicSet = set()

for item in items:
	
	topicId = item['topicId']
	topicSet.add(topicId)

for t in topicSet:
	
	d = db.discuss.find_one({ 'topicId' : t })
	topicName = d['topicName']
	topicDescription = d['topicDescriptionClean']
	semester = d['semester']

	db.topics.insert_one({
		'_id' : t,
		'topicName' : topicName,
		'topicDescription' : topicDescription,
		'semester' : semester
		})