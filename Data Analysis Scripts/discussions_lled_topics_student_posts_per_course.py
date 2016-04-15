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

items = db.PostsPerTopic.find({}, no_cursor_timeout=True)
courseSet = set()

for item in items:
		tId = item['_id']
		course = item['courseName']
		courseSet.add(course)

for c in courseSet:
	courseDict = {}
	numTopics = 0
	topics = db.PostsPerTopic.find( { 'courseName' : c } )
	

	for t in topics:
		postsPerStudent = t['postsPerStudent']
		numTopics += 1

		for p in postsPerStudent:
			numPosts = postsPerStudent[p]
			if p not in courseDict:
				courseDict.update( { p : numPosts } )
			else:
				courseDict[p] += numPosts
	db.PostsPerCourse.insert_one( { '_id' : c, 'postsPerStudent' : courseDict, 'numTopics' : numTopics } )


print(datetime.now() - start)