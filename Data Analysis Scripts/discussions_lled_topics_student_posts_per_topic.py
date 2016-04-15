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
		course = item['courseName']
		posts = db.discuss.find( { 'topicId' : tId, 'courseName' : course}, no_cursor_timeout=True)
		postDict = {}


		for p in posts:
			role = p['role']
			userId = p['userIdEncrypt']

			if role == "Student":
				if userId not in postDict:
					postDict.update({userId : 1})
				else:
					postDict[userId] += 1

		db.PostsPerTopic.insert_one( { '_id':tId, 'courseName' : course, 'postsPerStudent' : postDict } )


print(datetime.now() - start)