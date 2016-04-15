from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.topics.find({ 'lled' : True })

for item in items:
	courseName = item['courseName']
	tId = item['_id']

	if courseName[0:3] == 'XLS':
		shortCourseName = courseName[7:16]
	else:
		shortCourseName = courseName[0:9]

	db.topics.update_one(
		{ '_id' : tId },
		{
			'$set' : { 'shortCourseName' : shortCourseName }
		}, upsert=False
		)