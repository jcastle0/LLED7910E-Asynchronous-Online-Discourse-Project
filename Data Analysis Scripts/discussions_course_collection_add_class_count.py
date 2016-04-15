from pymongo import MongoClient
import pymongo
import json
import csv
from mongo_db_connect import db

courses = db.discussCourses.find({})

for course in courses:
	ouId = course['_id']

	items = db.discuss.find({ 'd2lid' : ouId })
	students = set()
	instructors = set()
	tas = set()

	for item in items:
		
		# User Variables
		userId = str(item['userIdEncrypt'])
		userRole = str(item['userRole']) # D2L User Code
		role = item['role'] # Human Readable Role

		if role == 'Student':
			students.add(userId)

		if role == 'Instructor':
			instructors.add(userId)

		if role == 'Teaching Assistant' or role == 'TA - Designer' or role == 'TA - Grader':
			tas.add(userId)
				
	db.discussCourses.update_one(
		{ '_id' : ouId },
		{
			'$set' : {
				"participantCount.students" : len(students),
				"participantCount.instructors" : len(instructors),
				"participantCount.teachingAssistants" : len(tas)
			},
		}, upsert=False
	)