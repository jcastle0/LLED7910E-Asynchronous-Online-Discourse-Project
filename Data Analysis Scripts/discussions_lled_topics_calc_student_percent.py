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

items = db.PostsPerCourse.find({}, no_cursor_timeout=True)

for item in items:
		course = item['_id']
		postsPerStudent = item['postsPerStudent']
		cData = db.lledCourses.find_one( { '_id' : course } )
		totalPosts = cData['totalStudentPosts']
		percentDict = {}

		for p in postsPerStudent:
			userId = p
			posts = postsPerStudent[p]
			percent = float(posts) / float(totalPosts)
			percentDict.update({userId : percent})

		db.PostsPerCourse.update_one( 
			{ '_id' : course },
			{
			'$set' : { 'percentPosts' : percentDict }
			}, upsert=False
		)

			

print(datetime.now() - start)