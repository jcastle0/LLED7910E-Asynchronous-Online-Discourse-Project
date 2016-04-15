from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

items = db.discuss.find({})
courses = set()

for item in items:
	
	# Course Variables
	ouId = item['d2lid'] # D2L Course Id
	semester = item['semester']
	courses.add(ouId)

for c in courses:

	item = db.discuss.find_one( { 'd2lid' : c } )

	courseName = item['courseName']
	semester = item['semester']

	if courseName[0:3] == 'XLS':
		course = courseName[7:16]
	else:
		course = courseName[0:9]

	print(c)
	print(course)
	print(semester)

	db.discussCourses.insert_one(
		{
		'_id' : c,
		'courseName' : course,
		'semester' : semester
		}
	)