from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db
import pprint
import time
from datetime import datetime

start = datetime.now()

pp = pprint.PrettyPrinter(indent=4)

items = db.topics.find({ 'lled' : True }, no_cursor_timeout=True)



for item in items:
		tId = item['_id']
		posts = db.discuss.find( { 'topicId' : tId}, no_cursor_timeout=True)
		postTimes = []


		for p in posts:
			role = p['role']
			datePosted = p['datePosted']
			postTimes.append({ 'role' : role, 'datePosted' : datePosted })

		db.postTimes.insert_one( { '_id' : tId, 'dateObjects' : postTimes})

print(datetime.now() - start)