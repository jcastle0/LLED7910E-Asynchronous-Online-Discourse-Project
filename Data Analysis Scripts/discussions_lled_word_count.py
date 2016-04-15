from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
from datetime import datetime

start = datetime.now()

items = db.topics.find({ 'lled' : True })

wordCountDict = { 'Student' : 0, 'Instructor' : 0, 'Teaching Assistant' : 0}

for item in items:
		tId = item['_id']

		posts = db.discuss.find( { 'topicId' : tId })

		for p in posts:
			wordCount = p['wordCount']
			role = p['role']

			if role == 'Student' or role == 'Instructor' or role == 'Teaching Assistant':
				wordCountDict[role] += wordCount

print(wordCountDict)
print(datetime.now() - start)