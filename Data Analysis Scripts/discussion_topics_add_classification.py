from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

with open('topics.json') as topicFile:
	topicData = json.load(topicFile)

for t in topicData:
	c = t['classification']
	tId = t['topicId']

	db.topics.update_one( 
		{ '_id' : tId },
		{
		'$set' : { 'classification' : c }
		}, upsert = False 
	)