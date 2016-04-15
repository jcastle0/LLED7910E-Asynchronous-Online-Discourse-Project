from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True })

for item in items:
	tId = item['_id']
	ouId = item['ouId']

	courseSet = set()

	p = db.discuss.find_one({ 'topicId' : tId, 'd2lid' : ouId })

	course = p['courseName']

	db.topics.update_one(
		{ '_id' : tId },
		{
			'$set' : {
				'courseName' : course
			}
		}, upsert=False
		)