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

totalCount = {}

for item in items:
		tId = item['_id']
		posts = db.discuss.find( { 'topicId' : tId }, no_cursor_timeout=True)


		for p in posts:
			role = p['role']
			courseName = p['courseName']

			if role == 'Student':
				if courseName not in totalCount:
					totalCount.update( { courseName : 1 })
				else:
					totalCount[courseName] += 1

for t in totalCount:
	name = t
	totalStudentPosts = totalCount[t]
	db.lledCourses.insert_one( { '_id' : name, 'totalStudentPosts' : totalStudentPosts} )

print(datetime.now() - start)