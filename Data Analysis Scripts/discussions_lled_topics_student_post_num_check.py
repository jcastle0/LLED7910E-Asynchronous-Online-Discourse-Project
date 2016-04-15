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

items = db.lledCourses.find({}, no_cursor_timeout=True)

for item in items:
		totalNum = item['totalStudentPosts']
		course = item['_id']
		print(course)
		print(totalNum)

		posts = db.PostsPerCourse.find( { '_id' : course } )

		for p in posts:
			allPosts = p['postsPerStudent']
			count = 0
			for a in allPosts:
				count += allPosts[a]
			print(count)
		print("-----------------------")
			

print(datetime.now() - start)